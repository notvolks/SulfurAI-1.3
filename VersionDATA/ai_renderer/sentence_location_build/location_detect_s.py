import os
import urllib.request
import langcodes
import pycountry
import fasttext
import numpy as np

def get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

# Call file paths
call = get_call_file_path()

# Constants
# Constants
MODEL_URL = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "lid.176.ftz")

DEFAULT_OVERRIDE = {
    "en": "England",  # generic English -> England
    "es": "Spain",
    "pt": "Portugal",
}
REGION_OVERRIDE = {
    'en-us': 'United States',
    'en-gb': 'United Kingdom',
    'en-au': 'Australia',
    'pt-br': 'Brazil',
    'zh-tw': 'Taiwan',
    # add more specific mappings as needed
}

# Dialect-specific keyword sets for English
US_KEYWORDS = {"color", "apartment", "truck", "fries", "elevator", "closet"}
UK_KEYWORDS = {"colour", "flat", "lorry", "crisps", "lift", "wardrobe"}


def download_fasttext_model():
    if not os.path.isfile(MODEL_PATH):
        print("Downloading fastText language ID model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Download complete.")


def load_model():
    download_fasttext_model()
    return fasttext.load_model(MODEL_PATH)

model = load_model()


def predict_location_viaLanguage(input_text):
    def safe_predict(text, k=5, threshold=0.0, label_prefix="__label__"):
        """
        Predict top-k language codes with fastText, return list of (code, prob).
        Coerce list inputs to a single string.
        """
        if not isinstance(text, str):
            text = " ".join(text)
        raw = model.f.predict(text, k, threshold, label_prefix)
        results = []
        for prob, lbl in raw:
            code = lbl.replace(label_prefix, "")
            results.append((code, float(prob)))
        return results

    def lang_to_country_with_dialect(lang_code_list, text):
        """
        Enhanced mapping: checks for dialect keywords in English text,
        then region-specific overrides, generic overrides, and CLDR defaults.
        Returns (country_name, confidence).
        """
        # Handle case with no predictions
        if not lang_code_list:
            return "Unknown", 0.0

        # Normalize text tokens
        if not isinstance(text, str):
            text_lc = set(" ".join(text).lower().split())
        else:
            text_lc = set(text.lower().split())

        # 0) Non-English codes use existing overrides
        for code, prob in lang_code_list:
            if not code.startswith("en"):
                lc = code.lower()
                if lc in REGION_OVERRIDE:
                    return REGION_OVERRIDE[lc], prob
                parts = code.split('-')
                if len(parts) == 2:
                    country_obj = pycountry.countries.get(alpha_2=parts[1].upper())
                    if country_obj:
                        return country_obj.name, prob
        # 1) Dialect heuristics for English
        if any(w in text_lc for w in US_KEYWORDS):
            return "United States", 1.0
        if any(w in text_lc for w in UK_KEYWORDS):
            return "United Kingdom", 1.0
        # 2) Region-specific overrides
        for code, prob in lang_code_list:
            lc = code.lower()
            if lc in REGION_OVERRIDE:
                return REGION_OVERRIDE[lc], prob
        # 3) Generic language overrides
        for code, prob in lang_code_list:
            lang = code.split('-')[0]
            if lang in DEFAULT_OVERRIDE:
                return DEFAULT_OVERRIDE[lang], prob
        # 4) CLDR default via langcodes
        first_code, first_prob = lang_code_list[0]
        locale = langcodes.Language.get(first_code).maximize()
        region = locale.region
        if region:
            country_obj = pycountry.countries.get(alpha_2=region)
            if country_obj:
                return country_obj.name, first_prob
        # Fallback
        return "Unknown", first_prob


    # Main prediction flow
    predictions = safe_predict(input_text)
    country, confidence = lang_to_country_with_dialect(predictions, input_text)
    file_path_ui_pred_loc = call.ui_predicted_location()
    file_path_ui_pred_loc_acc = call.ui_predicted_location_accuracy()
    with open(file_path_ui_pred_loc, "w", encoding="utf-8", errors="ignore") as file: file.write(str(country))
    with open(file_path_ui_pred_loc_acc, "w", encoding="utf-8", errors="ignore") as file: file.write(str(confidence * 100))
    return country, confidence




