import os,subprocess,sys
from datetime import datetime
from collections import Counter
def install(packages):
    package_string = ""

    if isinstance(packages, str):
        packages = [packages]

    for pkg in packages:
        try:
            if pkg == "pygame-ce":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-ce", "--upgrade"])
                print("pygame-ce installed successfully!")
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
                print(f"{pkg} installed successfully!")
        except (ModuleNotFoundError, PermissionError, TimeoutError, MemoryError) as error:
            print(f"An error occurred while installing {pkg}: {error}")
        except subprocess.CalledProcessError as error:
            print(f"Failed to install {pkg}. Error: {error}")


try: import tensorflow
except ImportError:
    install("tensorflow")
    print("-------tensorflow has been installed successfully.")
    try:
     import tensorflow
    except ImportError:
        print(f"Error while importing TensorFlow after installation. Restart Sulfur to fix the bug.")

from VersionDATA.ai_renderer import error
error = error.error
from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
from VersionDATA.verification.input_text import txt_data


def get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

call = get_call_file_path()

ARTIFACT_DIR = "VersionDATA/ai_renderer_2/tensorflowDependancies"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

import random
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress most TF logging (errors only)
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle
import os
import pandas as pd
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    gpu_usage = True
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)
else: gpu_usage = False


class SentenceIntentModel:
    def __init__(self):
        self.tokenizer = None
        self.sent_type_encoder = None
        self.intent_encoder = None
        self.model = None
        self.maxlen = None

    def build_model(self, sentences, sentence_types, intents):

        self.tokenizer = Tokenizer(oov_token="<OOV>")
        self.tokenizer.fit_on_texts(sentences)
        sequences = self.tokenizer.texts_to_sequences(sentences)
        padded = pad_sequences(sequences, padding='post')
        self.maxlen = padded.shape[1]


        self.sent_type_encoder = LabelEncoder()
        self.intent_encoder = LabelEncoder()
        y_sent = self.sent_type_encoder.fit_transform(sentence_types)
        y_intent = self.intent_encoder.fit_transform(intents)

        # Define the model
        input_layer = Input(shape=(self.maxlen,))
        x = Embedding(input_dim=1000, output_dim=16)(input_layer)
        x = GlobalAveragePooling1D()(x)
        x = Dense(16, activation='relu')(x)

        sent_type_out = Dense(len(self.sent_type_encoder.classes_), activation='softmax', name="sentence_type")(x)
        intent_out = Dense(len(self.intent_encoder.classes_), activation='softmax', name="intent")(x)
        self.model = Model(inputs=input_layer, outputs=[sent_type_out, intent_out])


        self.model.compile(
            loss={"sentence_type": "sparse_categorical_crossentropy", "intent": "sparse_categorical_crossentropy"},
            optimizer="adam",
            metrics={"sentence_type": "accuracy", "intent": "accuracy"}
        )

        # Train the model
        self.model.fit(padded, {"sentence_type": y_sent, "intent": y_intent}, epochs=10, verbose=0)

        # Save artifacts
        self.model.save(os.path.join(ARTIFACT_DIR, 'sentence_intent_model.keras'))
        pickle.dump(self.tokenizer, open(os.path.join(ARTIFACT_DIR, 'tokenizer.pkl'), 'wb'))
        pickle.dump(self.sent_type_encoder, open(os.path.join(ARTIFACT_DIR, 'sent_type_encoder.pkl'), 'wb'))
        pickle.dump(self.intent_encoder, open(os.path.join(ARTIFACT_DIR, 'intent_encoder.pkl'), 'wb'))

    def generate_dummy_data(self, num_samples):

        dummy_sentences = [
            "This is a random sentence.",
            "What do you mean?",
            "I don't understand.",
            "Can you help me?",
            "Wow, that's amazing!",
            "It's raining outside."
        ]
        dummy_sentence_types = ["question", "statement", "command", "exclamation"]
        dummy_intents = ["asking", "informing", "commanding", "expressing", "comparing"]
        sentences = []
        types = []
        intents = []
        for _ in range(num_samples):
            sentences.append(random.choice(dummy_sentences))
            types.append(random.choice(dummy_sentence_types))
            intents.append(random.choice(dummy_intents))
        return sentences, types, intents

    @staticmethod
    def load_training_data(file_path, min_samples=20):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return None
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()
            if df.empty or not {"sentence", "sentence_type", "intent"}.issubset(df.columns) or len(df) < min_samples:
                return None
            return df['sentence'].tolist(), df['sentence_type'].tolist(), df['intent'].tolist()
        except Exception:
            return None

    def predict_sentence(self, sentence):
        if self.model is None:
            self.model = load_model('sentence_intent_model.h5')
        if self.tokenizer is None:
            self.tokenizer = pickle.load(open('tokenizer.pkl', 'rb'))
        if self.sent_type_encoder is None:
            self.sent_type_encoder = pickle.load(open('sent_type_encoder.pkl', 'rb'))
        if self.intent_encoder is None:
            self.intent_encoder = pickle.load(open('intent_encoder.pkl', 'rb'))

        seq = self.tokenizer.texts_to_sequences([sentence])
        padded = pad_sequences(seq, padding='post', maxlen=self.maxlen)

        sent_pred, intent_pred = self.model.predict(padded,verbose=0)

        sent_type = self.sent_type_encoder.inverse_transform([np.argmax(sent_pred)])
        intent = self.intent_encoder.inverse_transform([np.argmax(intent_pred)])

        if file_path_path_versionDATA_name_sentences is not None:
            try:
                training_data_df = pd.read_csv(file_path_path_versionDATA_name_sentences)
                training_data_df.columns = training_data_df.columns.str.strip()

                # ✅ Add date column
                new_row = {
                    'sentence': sentence,
                    'sentence_type': sent_type[0],
                    'intent': intent[0],
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

                new_row_df = pd.DataFrame([new_row])

                training_data_df = pd.concat([training_data_df, new_row_df], ignore_index=True)

                training_data_df.to_csv(file_path_path_versionDATA_name_sentences, index=False)

                return sent_type[0], intent[0], training_data_df
            except Exception as e:
                print(f"Error while loading or saving training data: {e}")
                return sent_type[0], intent[0], ""

        return sent_type[0], intent[0], ""

    def evaluate_model(self, sentences, sentence_types, intents):
        sequences = self.tokenizer.texts_to_sequences(sentences)
        padded = pad_sequences(sequences, padding='post', maxlen=self.maxlen)

        y_sent = self.sent_type_encoder.transform(sentence_types)
        y_intent = self.intent_encoder.transform(intents)

        loss, sent_loss, intent_loss, sent_acc, intent_acc = self.model.evaluate(
            padded, {"sentence_type": y_sent, "intent": y_intent}, verbose=0
        )
        return sent_acc, intent_acc


def sentence_intent_and_infer():
    acc_sent_global = 0
    acc_intent_global = 0
    avg_accuracy_global = 0
    avg_sent_types = ""
    avg_intent_types = ""
    global file_path_path_versionDATA_name_sentences
    file_path_path_versionDATA_name_sentences = call.versionDATA_trainingdata_sentences()
    training = SentenceIntentModel.load_training_data(file_path_path_versionDATA_name_sentences)
    model_obj = SentenceIntentModel()
    if training:
        sentences, sentence_types, intents = training
    else:
        sentences, sentence_types, intents = model_obj.generate_dummy_data(50)
    model_obj.build_model(sentences, sentence_types, intents)

    # ----------------------USER
    prompt, too_long, re_was_subbed = txt_data.verify_input("string")
    user_input = prompt.strip()
    stype_user, sintent_user, _ = model_obj.predict_sentence(user_input)
    file_path_OutputData_Sentence_Intent_User = call.Sentence_Intent_User()
    file_path_OutputData_Sentence_Type_User = call.Sentence_Type_User()
    with open(file_path_OutputData_Sentence_Intent_User, "w", encoding="utf-8", errors="ignore") as file: file.write(sintent_user)
    with open(file_path_OutputData_Sentence_Type_User, "w", encoding="utf-8", errors="ignore") as file: file.write(stype_user)
    acc_sent_user, acc_intent_user = model_obj.evaluate_model(sentences, sentence_types, intents)
    #print(f"\n📊 Final Sentence Type Accuracy: {acc_sent:.2%}")
    #print(f"📊 Final Intent Accuracy: {acc_intent:.2%}")
    # ----------------------GLOBAL
    if os.access(file_path_path_versionDATA_name_sentences, os.R_OK):
        try:


            with open(file_path_path_versionDATA_name_sentences, 'r', encoding='utf-8') as file:
                file_contents = file.read()


            df = pd.read_csv(file_path_path_versionDATA_name_sentences)
            df.columns = df.columns.str.strip()


            sentences = df['sentence'].tolist()
            true_sent_types = df['sentence_type'].tolist()
            true_intents = df['intent'].tolist()


            def get_predictions(model, tokenizer, sentences, maxlen):
                sequences = tokenizer.texts_to_sequences(sentences)
                padded = pad_sequences(sequences, padding='post', maxlen=maxlen)


                sent_preds, intent_preds = model.predict(padded,verbose=0)


                sent_type_preds = np.argmax(sent_preds, axis=1)
                intent_preds = np.argmax(intent_preds, axis=1)

                return sent_type_preds, intent_preds


            true_sent_types_encoded = model_obj.sent_type_encoder.transform(true_sent_types)
            true_intents_encoded = model_obj.intent_encoder.transform(true_intents)

            # Get the predictions from the model
            pred_sent_types, pred_intents = get_predictions(model_obj.model, model_obj.tokenizer, sentences,
                                                            model_obj.maxlen)


            sent_type_accuracy = accuracy_score(true_sent_types_encoded, pred_sent_types)
            intent_accuracy = accuracy_score(true_intents_encoded, pred_intents)


            avg_accuracy = (sent_type_accuracy + intent_accuracy) / 2

            acc_sent_global = sent_type_accuracy #sentence accuracy
            acc_intent_global = intent_accuracy #intent accuracy
            avg_accuracy_global = avg_accuracy #average accuracy
            avg_sent_types =  model_obj.sent_type_encoder.inverse_transform(pred_sent_types)
            avg_intent_types = model_obj.intent_encoder.inverse_transform(pred_intents)
            avg_sent_types = Counter(avg_sent_types).most_common(1)[0][0] #sentence type
            avg_intent_types = Counter(avg_intent_types).most_common(1)[0][0] #intent type

            try:

                file_path_OutputData_Sentence_Intent_Global = call.Sentence_Intent_Global()
                file_path_OutputData_Sentence_Type_Global = call.Sentence_Type_Global()
                file_path_OutputData_Sentence_Accuracy_Average_Global = call.Sentence_Accuracy_Average_Global()
                file_path_OutputData_Sentence_Intent_Accuracy_Global = call.Sentence_Accuracy_Intent_Global()
                file_path_OutputData_Sentence_Type_Accuracy_Global = call.Sentence_Accuracy_Type_Global()
                with open(file_path_OutputData_Sentence_Intent_Global, "w", encoding="utf-8", errors="ignore") as file: file.write(avg_intent_types)
                with open(file_path_OutputData_Sentence_Type_Global, "w", encoding="utf-8", errors="ignore") as file: file.write(avg_sent_types)
                with open(file_path_OutputData_Sentence_Accuracy_Average_Global, "w", encoding="utf-8", errors="ignore") as file: file.write(str(avg_accuracy_global * 100))
                with open(file_path_OutputData_Sentence_Intent_Accuracy_Global, "w", encoding="utf-8", errors="ignore") as file:  file.write(str(acc_intent_global * 100))
                with open(file_path_OutputData_Sentence_Type_Accuracy_Global, "w", encoding="utf-8",errors="ignore") as file: file.write(str(acc_sent_global * 100))

            except (AttributeError,TypeError,FileNotFoundError,OSError,IOError,UnicodeEncodeError,NameError) as e:
                print(f"Output_WRITE error: {e}")
                error("er1", "Output_WRITE", "Error writing output for sentence_detectAndInfer_s.py", "13")
        except PermissionError as e:
            print(f"Permission error: {e}")
            error("er1", "Output_PERMISSION", "Error getting permission for sentence_detectAndInfer_s.py", "14")
        except Exception as e:
            print(f"An error occurred: {e}")
            error("er1", "Output_EXCEPTION", "Error general for sentence_detectAndInfer_s.py", "15")
    else:
        print(f"Cannot access the file. Please check the permissions for: {file_path_path_versionDATA_name_sentences}")
        error("er1", "Output_PERMISSION_ACCESS", "Error getting permission to access VERSIONDATA/SENTENCE (GENERAL) for sentence_detectAndInfer_s.py", "16")


    return stype_user, sintent_user,acc_sent_user,acc_intent_user,avg_sent_types,avg_intent_types,acc_sent_global,acc_intent_global,avg_accuracy_global #Returns sentence type and sentence intent


