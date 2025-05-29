import os
import re
import urllib.request
import langcodes
import pycountry
import fasttext
import numpy as np
import random
_orig_np_array = np.array

# override np.array to drop any 'copy' kwarg
def _array_override(a, *args, **kwargs):
    kwargs.pop('copy', None)
    return _orig_np_array(a, *args, **kwargs)

# install the override
np.array = _array_override
import joblib
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import NotFittedError
from sklearn.dummy import DummyClassifier


# === CALL FILE PATH SETUP ===

def get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

call = get_call_file_path()

# === CONSTANTS & OVERRIDES ===

MODEL_URL = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "lid.176.ftz")

default_override = {"en": "England", "es": "Spain", "pt": "Portugal"}
region_override = {
    'en-us': 'United States', 'en-gb': 'United Kingdom', 'en-au': 'Australia',
    'pt-br': 'Brazil', 'zh-tw': 'Taiwan'
}
US_KEYWORDS = {"color", "apartment", "truck", "fries", "elevator", "closet"}
UK_KEYWORDS = {"colour", "flat", "lorry", "crisps", "lift", "wardrobe"}

# === FASTTEXT LANGUAGE MODEL ===

def download_fasttext_model():
    if not os.path.isfile(MODEL_PATH):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

def load_fasttext_model():
    download_fasttext_model()
    return fasttext.load_model(MODEL_PATH)

fasttext_model = load_fasttext_model()

# === TRAINING DATA FILE ===

training_data_location = call.training_data_location()

# Helpers to load/save training samples

def load_training_data(path):
    strings, labels, accuracies = [], [] , []
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 3:
                    strings.append(",".join([parts[0]]))
                    labels.append(parts[1])
                    accuracies.append(float(parts[2]))
    return strings, labels,accuracies

def save_training_sample(path, string, label,confidence):


    line = f"{string}\t{label}\t{confidence * 100}"  # target line

    existing = set()
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            # Build a set of "string<TAB>label" lines without newlines
            existing = {l.rstrip("\n") for l in f}

    if line in existing:
        return

    # Write the new line
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# === COUNTRY CLASSIFIER SETUP ===

class CountryClassifier:
    def __init__(self, ngram_range=(2,5), max_features=5000, use_regex=True):
        self.char_vec = TfidfVectorizer(analyzer='char', ngram_range=ngram_range, max_features=max_features)
        self.use_regex = use_regex
        self.model = LogisticRegression(max_iter=300)
        self.is_dummy = False  # flag to track dummy fallback

    def _regex_feats(self, s):
        return [
            bool(re.match(r"^\+\d", s)),
            bool(re.search(r"\.\w{2,3}$", s)),
            any(ch in 'éèàåø' for ch in s),
            s.isupper()
        ]

    def fit(self, strings, countries):
        Xc = self.char_vec.fit_transform(strings)
        if self.use_regex:
            Xr = np.array([self._regex_feats(s) for s in strings])
            X = hstack([Xc, Xr])
        else:
            X = Xc

        unique_labels = set(countries)
        if len(unique_labels) < 2:
            self.model = DummyClassifier(strategy="most_frequent")
            self.is_dummy = True
        else:
            self.model = LogisticRegression(max_iter=300)
            self.is_dummy = False

        self.model.fit(X, countries)

    def predict(self, s):
        txt = s if isinstance(s, str) else ' '.join(s)
        Xc = self.char_vec.transform([txt])
        if self.use_regex:
            Xr = np.array([self._regex_feats(txt)])
            X = hstack([Xc, Xr])
        else:
            X = Xc

        probs = self.model.predict_proba(X)[0]
        idx = np.argmax(probs)
        return self.model.classes_[idx], probs[idx]

    def save(self, dir_path):
        os.makedirs(dir_path, exist_ok=True)
        joblib.dump(self.char_vec, os.path.join(dir_path, 'vec.joblib'))
        joblib.dump(self.model, os.path.join(dir_path, 'model.joblib'))

    def load(self, dir_path):
        vec_path = os.path.join(dir_path, 'vec.joblib')
        model_path = os.path.join(dir_path, 'model.joblib')
        if os.path.isfile(vec_path) and os.path.isfile(model_path):
            self.char_vec = joblib.load(vec_path)
            self.model = joblib.load(model_path)
        else:
            raise NotFittedError

# Initialize classifier
classifier = CountryClassifier()
models_dir = os.path.join(BASE_DIR, 'country_models')

# Load existing model or train fresh on training data
strings, labels, accuracies = load_training_data(training_data_location)
if len(strings) < 3:
    # fallback dummy
    strings = ['+1 555 1234', '.us', '.uk']
    labels = ['United States', 'United States', 'United Kingdom']
classifier.fit(strings, labels)
classifier.save(models_dir)

# === LANGUAGE-BASED MAP ===

def predict_location_via_language(text, tag_trainer):
    import pycountry
    import langcodes

    def map_code_to_country(code):
        code = code.lower()

        # 1. Region override (e.g., en-gb)
        if code in region_override:
            return region_override[code]

        # 2. Country from hyphenated locale (e.g., "fr-fr")
        parts = code.split("-")
        if len(parts) == 2:
            c = pycountry.countries.get(alpha_2=parts[1].upper())
            if c:
                return c.name

        # 3. Default language override (e.g., "es" → Spain)
        lang = code.split("-")[0]
        if lang in default_override:
            return default_override[lang]

        # 4. Fallback to langcodes (e.g., en → maximize → en-GB)
        try:
            locale = langcodes.Language.get(code).maximize()
            if locale.territory:
                c = pycountry.countries.get(alpha_2=locale.territory)
                if c:
                    return c.name
        except:
            pass

        return "Unknown"

    if not isinstance(text, str):
        text = " ".join(text)

    tokens = set(text.lower().split())

    if not tag_trainer == "None":
        country = map_code_to_country(tag_trainer)
        return country, 1.0

    # Predict language if not provided
    raw_labels, raw_probs = fasttext_model.predict(text, k=5, threshold=0.0)
    raw_probs = list(raw_probs)
    labels = [lbl.replace("__label__", "") for lbl in raw_labels]
    preds = list(zip(labels, raw_probs))

    # Keyword heuristics
    if any(w in tokens for w in US_KEYWORDS):
        return "United States", 1.0
    if any(w in tokens for w in UK_KEYWORDS):
        return "United Kingdom", 1.0

    # Try mapping from predicted codes
    for code, p in preds:
        country = map_code_to_country(code)
        if country != "Unknown":
            return country, p

    return "Unknown", preds[0][1] if preds else 0.0


# === COMBINED PREDICTION FUNCTION ===

def predict_location(input_text,tag_trainer):
    # classifier prediction
    clf_country, clf_conf = classifier.predict(input_text)
    # fastText prediction
    lang_country, lang_conf = predict_location_via_language(input_text,tag_trainer)

    # combine
    if clf_country == lang_country:
        final_country = clf_country
        final_conf = (clf_conf + lang_conf) / 2
    else:
        if clf_conf > lang_conf:
            final_country, final_conf = clf_country, clf_conf
        else:
            final_country, final_conf = lang_country, lang_conf

    # write UI outputs
    with open(call.ui_predicted_location(), 'w', encoding='utf-8') as f:
        f.write(final_country)
    with open(call.ui_predicted_location_accuracy(), 'w', encoding='utf-8') as f:
        f.write(str(final_conf * 100))

    # append to training data if confident
    if final_conf >= 0.5:
        save_training_sample(training_data_location, input_text, final_country,final_conf)
        # reload full data
        strs, labs, accs = load_training_data(training_data_location)
        # only refit if there are at least two distinct labels
        if len(set(labs)) > 1:
            classifier.fit(strs, labs)
            classifier.save(models_dir)
        else:
            # not enough classes to retrain yet
            pass

    return final_country, final_conf

# === USAGE ===

