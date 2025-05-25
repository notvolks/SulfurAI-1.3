from VersionDATA.ai_renderer import module_restore_trainingData
from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
from VersionDATA.verification.input_text import txt_data
call = call_file_path.Call()
file_path_settings_name_extra_device = call.settings_extra_debug()

###these are settings to add to the settings.py
with open(file_path_settings_name_extra_device, "r", encoding="utf-8", errors="ignore") as file:
    extra_debug = file.readlines()  #extra debug print statements


file_path_training_data_sk_backup = call.backup_training_data_sk()
file_path_training_data_backup = call.backup_training_data()



from tqdm import tqdm
import math,random,datetime,re,time,logging

import language_tool_python,langdetect

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from sklearn.model_selection import GridSearchCV
from sklearn.dummy import DummyClassifier
import numpy as np
import os
from VersionDATA.ai_renderer import error
global Device_Accuracy, hours, minutes, seconds, total_time_ms
global CapitalAmountInputData

brick_out = error.brick_out
write_error = error.write_error
error = error.error
(folder_path_trainingData_grammar, folder_path_trainingData_grammar_name, file_path_trainingData_grammar) = call.grammar()

current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
folder_path_input = os.path.join(current_dir_i, 'DATA')
file_name_input = 'Input.txt'  # Debugger variables
file_name_attributes = "Attributes.txt"
file_name_output = "Output.txt"
file_path_input = os.path.join(folder_path_input, file_name_input)
file_path_attributes = os.path.join(folder_path_input, file_name_attributes)
file_path_output = os.path.join(folder_path_input, file_name_output)

os.makedirs(folder_path_input, exist_ok=True)

folder_path_verify = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DATA/dependancy_data/QVOL')
file_name_verify = "vrs.txt"
file_path_verify = os.path.join(folder_path_verify, file_name_verify)

#####################Attributes_device
Attribute_Device_Result = "NOT_SET"

if "yes" in extra_debug:
    if globals().get("__caller__") == "__main__":
        print("Commencing index:")
if os.path.exists(file_path_attributes):

    with open(file_path_attributes, 'r') as file:


        lines_a = file.readlines()
        if lines_a:
            for line in lines_a:
                if 'DEVICE : NOT_SET' in line: Attribute_Device_Result = "NOT_SET"
                if 'DEVICE : MOBILE(OTHER)' in line: Attribute_Device_Result = "MOBILE_OTHER"
                if 'DEVICE : DESKTOP' in line: Attribute_Device_Result = "DESKTOP"
        else:
            if "yes" in extra_debug:
                if globals().get("__caller__") == "__main__":
                    print("No attributes found, continuing...")
                Attribute_Device_Result = "NOT_SET"

else:
    error("er1", "DEPENDANCY_FILE", "ATTRIBUTES.TXT", "3")




#### DEVICE ATTRIBUTE






#####################

def debug():

    if os.path.exists(file_path_input):  # Checks for input
        with open(file_path_input, 'r', encoding="utf-8") as file:
            lines = file.readlines()

            if lines:
                if globals().get("__caller__") == "__main__":
                    print(f"Input found: {', '.join(lines)}")
                    print("Processing...")
                try:

                    def Capitals(list):  # Checks capitals and non-capitals
                        Sum = 0
                        for sublist in list:
                            for line in sublist:
                                Sum += sum(1 for char in line if char.isupper())
                        return Sum

                    def ReverseCapitals(list):
                        Sum = 0
                        for sublist in list:
                            for line in sublist:
                                Sum += sum(1 for char in line if not char.isupper())
                        return Sum

                    input_data,too_long,re_was_subbed = txt_data.verify_input("string")
                    compre_input_data = [list(s) for s in input_data]  # Individual strings

                    CapitalAmountInputData = Capitals(compre_input_data)
                    ReverseCapitalAmountInputData = ReverseCapitals(compre_input_data)

                    # Grammar = [".",",","'"] # re-link to a txt file - DISABLED DUE TO TRAINING DATA REPLACING IT
                    GrammarCount = 0

                    with open(file_path_trainingData_grammar, 'r', encoding="utf-8",
                              errors="ignore") as file:  # Checks for grammar training data
                        lines_grammar = file.readlines()
                        if lines_grammar:
                            first_line = lines_grammar[0].strip(",")
                            first_line_list = [char for char in first_line]

                            Grammar = first_line_list

                            for item in Grammar:
                                GrammarCount += sum(sublist.count(item) for sublist in compre_input_data)
                    if globals().get("__caller__") == "__main__":
                        print("Processing finished with no errors.")  # Error marker



                except (TypeError, MemoryError, RecursionError, UnicodeDecodeError) as e:
                    error("er2", "Processing", str(e),"1")
                    brick_out(1000)
            else:
                if globals().get("__caller__") == "__main__":
                    print("No input log was found. Go into the file: DATA/Input.txt to enter an INPUT!")
                write_error("No input log was found. Go into the file: DATA/Input.txt to enter an INPUT!",
                            "debug_error")
                brick_out(1000)
    else:
        error("er1", "DEPENDANCY_FILE", "INPUT.TXT","2")  # Pre-historic checker. Not needed but kept for funsies
        brick_out(1000)

    if not os.path.exists(file_path_attributes):
        error("er1", "DEPENDANCY_FILE", "ATTRIBUTES.TXT","3")
        brick_out(1000)

    if not os.path.exists(file_path_output):
        error("er1", "DEPENDANCY_FILE", "OUTPUT.TXT","4")
        brick_out(1000)
    return CapitalAmountInputData,ReverseCapitalAmountInputData,lines,GrammarCount, compre_input_data,input_data
CapitalAmountInputData,ReverseCapitalAmountInputData,lines,GrammarCount, compre_input_data,input_data = debug()
class DataLog:
    def check_input(self):
        call_file_input()
        if broadcast_verify(file_link):
            pass
        else:
            error("er1", "DEPENDANCY_FILE", "INPUT.TXT","2")

    def check_attributes(self):
        call_file_attributes()
        if broadcast_verify(file_link_a):
            pass
        else:
            error("er1", "DEPENDANCY_FILE", "ATTRIBUTES.TXT","3")

    def check_output(self):
        call_file_output()
        if broadcast_verify(file_link_o):
            pass
        else:
            error("er1", "DEPENDANCY_FILE", "OUTPUT.TXT","4")

def instant_shutdown(reason):
    try:
        exit()
    except (ImportError, SystemExit) as y:
        print(f"InstantShutDown-Initiated: {reason} Testing exit: Value:Exception// exit(sys):{y}")
        time.sleep(5)
        quit()

class Sulfur:  # Hardcoded sulfur values
    @staticmethod
    def think(text):
        if globals().get("__caller__") == "__main__":
            print(f"-------Sulfur is thinking... {text}")

class Sk:
    def __init__(self):
        self.model = None
        self.labels = ["NOT_SET", "DESKTOP", "MOBILE(OTHER)"]

    def label_sk_data(self, input_label):

        try:
            # Convert input to float, floor it, then cast to integer

            check_ver_label = type(input_label)
        except ValueError:
            logging.warning(f"Invalid input for conversion: '{input_label}'. Returning -1.")
            return -1

        # Attempt to find the integer label in the list
        try:

            return self.labels.index(input_label)
        except ValueError:
            logging.warning(f"Unknown label '{input_label}'. Returning -1.")
            return -1

    def write_training_data_sk(self, input_text, accuracy, label, file_path):
        cleaned_input_text = input_text.strip()


        output_line = f"{cleaned_input_text},{accuracy},{label}"

        with open(file_path, "a", encoding="utf-8", errors="ignore") as file:
            file.write(output_line + '\n')

    def prepare_data_sk(self, file_path):
        texts = []
        labels = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    text, accuracy, label = line.strip().split(",")
                    texts.append(text)
                    labels.append(int(label))
                except ValueError as e:
                    if "yes" in extra_debug:
                        print(f"Skipping invalid line: {line.strip()} - {e}")
                    else:
                        continue
        return texts, labels

    def train_model(self, texts, labels):
        if not texts or not labels:
            print("No training data_available. Sending backup data to replace the training data.")
            module_restore_trainingData.restore_data_hardforce()
            raise ValueError("No training data available")


        unique_labels = set(labels)
        label_counts = Counter(labels)
        if "yes" in extra_debug:
            print(f"Class distribution: {dict(label_counts)}")

        if len(unique_labels) < 2:
            print("Warning: Only one class present in the training data. Attempting to use DummyClassifier.")
            try:
                self.model = DummyClassifier(strategy="constant", constant=list(unique_labels)[0])
                self.model.fit(texts, labels)
            except (ValueError,TypeError,ImportError):
                #change tmrw
                print("Failed to use DummyClassifier. Resetting training data.")
                module_restore_trainingData.restore_data_hardforce()
                print("Now restarting DummyClassifier")
                self.model = DummyClassifier(strategy="constant", constant=list(unique_labels)[0])
                self.model.fit(texts, labels)

            return

        min_samples = min(label_counts.values())
        n_splits = min(3, min_samples)  # Use at most 3 splits, no more than the smallest class size

        if n_splits > 1 and min(label_counts.values()) < n_splits:
            n_splits = min(label_counts.values())

        if n_splits < 2:
            print("Warning: Not enough samples for stratified cross-validation. Using a single split.")
            n_splits = 1

        X_train, X_test, y_train, y_test = train_test_split(
            texts, labels, test_size=0.2, random_state=42, stratify=labels
        )

        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 3), max_features=10000, stop_words='english')),
            ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
        ])

        param_grid = {
            'clf__n_estimators': [50, 100],
            'clf__max_depth': [None, 10],
            'clf__min_samples_split': [2, 5]
        }

        if n_splits > 1:
            grid_search = GridSearchCV(pipeline, param_grid,
                                       cv=StratifiedKFold(n_splits=n_splits), n_jobs=-1)
            grid_search.fit(X_train, y_train)
            self.model = grid_search.best_estimator_
            if "yes" in extra_debug:
                if globals().get("__caller__") == "__main__":
                    print(f"Best hyperparameters: {grid_search.best_params_}")
        else:
            print("Warning: Not enough samples for cross-validation. Using default hyperparameters.")
            self.model = pipeline
            self.model.fit(X_train, y_train)

        # You might print training/test scores here if desired

        if n_splits > 1:
            cv = StratifiedKFold(n_splits=n_splits)
            cv_scores = cross_val_score(self.model, texts, labels, cv=cv)

    def predict_device(self, input_text):
        if self.model is None:
            raise ValueError("Model has not been trained yet")
        prediction = self.model.predict([input_text])
        return self.labels[prediction[0]]

    def label_write_sk_data(self):

        # Use globals: file_path_training_data_sk and input_data

        global input_data, Device_Result, Device_Accuracy, file_path_training_data_sk
        instance = Ai()

        folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk = call.training_data_sk()

        label = self.label_sk_data(Device_Result)
        if label != -1:
            self.write_training_data_sk(''.join(input_data), Device_Accuracy, label, file_path_training_data_sk)
            texts, labels = self.prepare_data_sk(file_path_training_data_sk)

            if texts and labels:
                self.train_model(texts, labels)
            else:
                print("No training data available for SK model.")
                print("Attempting to resort to backup data.")
                try:
                    label = self.label_sk_data(Device_Result)
                    if label != -1:
                        texts, labels = self.prepare_data_sk(file_path_training_data_sk_backup)

                        if texts and labels:
                            self.train_model(texts, labels)
                except FileNotFoundError:
                    print("No backup training data available for SK model.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                    error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA","5")
                except ValueError:
                    print("Value Error backup training data found for SK model.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                    error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA : VALUE ERROR","6")
                except Exception as e:
                    print(f"{e} backup training data found for SK model.")
                    print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: restart sulfur.")
                    error("er1", "DEPENDANCY_FILE", f"BACKUP TRAINING DATA : {e}","7")









class Ai():
    def __init__(self):

        self.machine_model_checkDevice_result = 0
        self.machine_model_checkDevice_result_accuracy = 0
        self.accuracy = 0

    def prepare_data(self, file_path, input_data):

        if isinstance(input_data, list):
            input_data,too_long,re_was_subbed = ",".join(txt_data.verify_input("string"))
        training_data = []
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                read_lines = line.strip().split(",")
                # Remove any empty strings
                read_lines = [s for s in read_lines if s.strip()]
                if read_lines:
                    training_data.extend(read_lines)

        # Debug: show the training data


        # Find indexes where the input_data appears in the entry.
        indexes = []
        for i, entry in enumerate(training_data):
            # Debug: show the comparison details.

            if input_data.strip() in entry:
                indexes.append(i)

        # Debug: show the matching indexes.


        if indexes:
            self.machine_model_checkDevice_result = 0
            self.accuracy = 0
            highest_accuracy = 0  # To store the highest accuracy found

            for index in indexes:
                entry = training_data[index]
                if "[DEVICE : MOBILE(OTHER)]" in entry:
                    self.machine_model_checkDevice_result = 2
                elif "[DEVICE : DESKTOP]" in entry:
                    self.machine_model_checkDevice_result = 1

                match = re.search(r"\[DEVICE_ACCURACY : ([\d.]+)\]", entry)
                if match:
                    accuracy_value = float(match.group(1))
                    highest_accuracy = max(highest_accuracy, accuracy_value)

            self.accuracy = highest_accuracy
        else:
            self.machine_model_checkDevice_result = 0
            self.accuracy = 0

        self.machine_model_checkDevice_result_accuracy = self.accuracy if self.accuracy != 0 else 20

        # Debug: print all matched entries



    def train_data_model_checkdv(self, input_text, items_list):

        normal_input = str(input_text).strip().lower()
        for index, item in enumerate(items_list):
            normal_item = item.strip().lower()
            if normal_input in normal_item:
                return index
        return -1

    def check_grammar(self):
        try:
            language_code = langdetect.detect(str(input_data))
        except Exception as e:
            print(f"{e} has occured. Default language set to English-UK.")
            language_code = 'en'
        supported_languages = ['en', 'es', 'fr', 'de']  # Add other supported codes here

        if language_code not in supported_languages:
            print(f"Warning: The language '{language_code}' is not supported. Defaulting to English.")
            language_code = 'en'

        try:
            tool = language_tool_python.LanguageTool(language_code)
            grammar_errors = len(tool.check(str(input_data)))
        except Exception as e:
            print(f"{e} has occured. Grammar Errors are set to 1.")
            grammar_errors = 1
        return grammar_errors

    def check_device(self): # wip, needs working on [Ai function to call a device]
        call = call_file_path.Call()
        ai_process_instance = ai_process_cd()





        global machine_model_checkDevice_result, machine_model_checkDevice_result_accuracy, accuracy
        global prediction, Device_Accuracy, Device_Result, Attribute_Device_Result

        # Training data for AI
        folder_path_training_data, folder_path_training_data_name, file_path_training_data = call.training_data()


        Sulfur_Output_Device_Desktop_Percent = 0
        Sulfur_Output_DeviceMobileORother_Percent = 0


        if CapitalAmountInputData > 0:
            Sulfur_Output_DeviceMobileORother_Percent += (CapitalAmountInputData / 5)
        else:
            Sulfur_Output_DeviceMobileORother_Percent += (CapitalAmountInputData / 3.5)


        if ReverseCapitalAmountInputData > 0:

            norm_value = len(', '.join(lines))
            Sulfur_Output_Device_Desktop_Percent += (ReverseCapitalAmountInputData / norm_value)


        norm_value = len(', '.join(lines))
        if GrammarCount > 0:
            if GrammarCount > 2:

                Sulfur_Output_DeviceMobileORother_Percent += int(
                    GrammarCount / norm_value / (GrammarCount / norm_value))
            else:
                Sulfur_Output_DeviceMobileORother_Percent += int(GrammarCount / norm_value / (GrammarCount / 5))
        else:
            Sulfur_Output_Device_Desktop_Percent += 0.1


        if compre_input_data:
            first_instance = str(compre_input_data[0])
            if len(first_instance) > 2 and first_instance[2].isupper():
                Sulfur_Output_DeviceMobileORother_Percent += int(
                    (CapitalAmountInputData + GrammarCount / norm_value) / ((CapitalAmountInputData / 2.5) + 1)
                )


        ai = Ai()
        try:
         ai.prepare_data(file_path_training_data, input_data)
        except Exception:
            print("Error with training data.")
            print("Attempting to resort to backup data.")
            try:
                ai.prepare_data(file_path_training_data_backup, input_data)
            except FileNotFoundError:
                print("No backup training data available for C_D_S.ai model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA","5")
            except ValueError:
                print("Value Error backup training data found for C_D_S.ai model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA : VALUE ERROR","6")
            except Exception as e:
                print(f"{e} backup training data found for C_D_S.ai model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", f"BACKUP TRAINING DATA : {e}","7")

        # Retrieve AI computed values
        machine_model_checkDevice_result = ai.machine_model_checkDevice_result
        machine_model_checkDevice_result_accuracy = ai.machine_model_checkDevice_result_accuracy
        accuracy = ai.accuracy  # THIS IS A FIX IF THE VARIABLE IS NOT CALLED

        # Adjust percentages based on AI’s machine model result
        if machine_model_checkDevice_result == 1:
            Sulfur_Output_Device_Desktop_Percent = (
                    Sulfur_Output_Device_Desktop_Percent *
                    (0.5 + machine_model_checkDevice_result_accuracy / (
                                machine_model_checkDevice_result_accuracy + 10) / 2)
                    + 0.5
            )
        if machine_model_checkDevice_result == 2:
            Sulfur_Output_DeviceMobileORother_Percent = (
                    Sulfur_Output_DeviceMobileORother_Percent *
                    (0.5 + machine_model_checkDevice_result_accuracy / (
                                machine_model_checkDevice_result_accuracy + 10) / 2)
                    + 0.5
            )

        # Process training data for SK model
        folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk = call.training_data_sk()
        sk = Sk()
        texts, labels = sk.prepare_data_sk(file_path_training_data_sk)

        if texts and labels:
            try:
                sk.train_model(texts, labels)
                # Prediction: use provided input data
                input_text_for_prediction = input_data[0] if input_data else "default text"
                prediction = sk.predict_device(input_text_for_prediction)


                # Adjust percentages based on prediction result
                if prediction == "DESKTOP":
                    Sulfur_Output_Device_Desktop_Percent = (
                            Sulfur_Output_Device_Desktop_Percent *
                            (0.5 + machine_model_checkDevice_result_accuracy / (
                                        machine_model_checkDevice_result_accuracy + 10) / 2)
                            + 0.5
                    )
                elif prediction == "MOBILE(OTHER)":
                    Sulfur_Output_DeviceMobileORother_Percent = (
                            Sulfur_Output_DeviceMobileORother_Percent *
                            (0.5 + machine_model_checkDevice_result_accuracy / (
                                        machine_model_checkDevice_result_accuracy + 10) / 2)
                            + 0.5
                    )
            except Exception as e:
                print(f"Error in model training or prediction: {e}")
        else:
            print("No training data available for SK model.")
            print("Attempting to resort to backup data.")
            try:
                texts, labels = sk.prepare_data_sk(file_path_training_data_sk_backup)
                if texts and labels:
                    try:
                        sk.train_model(texts, labels)
                        # Prediction: use provided input data
                        input_text_for_prediction = input_data[0] if input_data else "default text"
                        prediction = sk.predict_device(input_text_for_prediction)

                        # Adjust percentages based on prediction result
                        if prediction == "DESKTOP":
                            Sulfur_Output_Device_Desktop_Percent = (
                                    Sulfur_Output_Device_Desktop_Percent *
                                    (0.5 + machine_model_checkDevice_result_accuracy / (
                                            machine_model_checkDevice_result_accuracy + 10) / 2)
                                    + 0.5
                            )
                        elif prediction == "MOBILE(OTHER)":
                            Sulfur_Output_DeviceMobileORother_Percent = (
                                    Sulfur_Output_DeviceMobileORother_Percent *
                                    (0.5 + machine_model_checkDevice_result_accuracy / (
                                            machine_model_checkDevice_result_accuracy + 10) / 2)
                                    + 0.5
                            )
                    except Exception as e:
                        print(f"Error in model training or prediction: {e}")
            except FileNotFoundError:
                print("No backup training data available for SK model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA","5")
            except ValueError:
                print("Value Error backup training data found for SK model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", "BACKUP TRAINING DATA : VALUE ERROR","6")
            except Exception as e:
                print(f"{e} backup training data found for SK model.")
                print("!!!!!!!!!!!!!!!!!!!!!!!Recommended action: install new version")
                error("er1", "DEPENDANCY_FILE", f"BACKUP TRAINING DATA : {e}","7")



        # Calculate Device Accuracy
        total_predictions = Sulfur_Output_Device_Desktop_Percent + Sulfur_Output_DeviceMobileORother_Percent
        if total_predictions > 0:
            correct_predictions = max(Sulfur_Output_Device_Desktop_Percent, Sulfur_Output_DeviceMobileORother_Percent)
            Device_Accuracy = (correct_predictions / total_predictions) * 100
        else:
            Device_Accuracy = 0

        if Device_Accuracy >= 100:
            Device_Accuracy = 99.9

        _, _, file_path_OutputData_name_Device_accuracy = call.device_accuracy()
        with open(file_path_OutputData_name_Device_accuracy,"w") as file:
            file.write(f"{Device_Accuracy}")


        if Attribute_Device_Result == "DESKTOP":
            Sulfur_Output_Device_Desktop_Percent += Sulfur_Output_DeviceMobileORother_Percent * 2
        elif Attribute_Device_Result == "MOBILE(OTHER)":
            Sulfur_Output_DeviceMobileORother_Percent += Sulfur_Output_Device_Desktop_Percent * 2


        file_path_OutputData_name_Device = call_file_path.file_path_OutputData_name_Device
        ###########Grammar########

        if Sulfur_Output_Device_Desktop_Percent > Sulfur_Output_DeviceMobileORother_Percent:                                          #takes the difference of mobile and dekstop predictions and adds it to the grammar errors
            start_grammar_weight = Sulfur_Output_Device_Desktop_Percent - Sulfur_Output_DeviceMobileORother_Percent
            if input_data:
                grammar_errors = self.check_grammar()
            else:
                print("Warning: Input data is empty. Grammar checking skipped.")
                grammar_errors = 0
            if start_grammar_weight > grammar_errors: Sulfur_Output_Device_Desktop_Percent += ((0.5 + start_grammar_weight - grammar_errors / ( start_grammar_weight - grammar_errors + 10) / 2)+ 0.5) / (Sulfur_Output_Device_Desktop_Percent * 3)
            else:
                grammar_placeholder = grammar_errors / (math.ceil(Sulfur_Output_DeviceMobileORother_Percent) + 1)
                Sulfur_Output_Device_Desktop_Percent += ((0.5 + grammar_placeholder / (grammar_placeholder) / 2) + 0.5) / (Sulfur_Output_Device_Desktop_Percent * 3)

        if Sulfur_Output_Device_Desktop_Percent < Sulfur_Output_DeviceMobileORother_Percent:
            start_grammar_weight = Sulfur_Output_DeviceMobileORother_Percent - Sulfur_Output_Device_Desktop_Percent
            if input_data:
                grammar_errors = self.check_grammar()
            else:
                print("Warning: Input data is empty. Grammar checking skipped.")
                grammar_errors = 0
            if start_grammar_weight > grammar_errors:
                Sulfur_Output_DeviceMobileORother_Percent += ((0.5 + start_grammar_weight - grammar_errors / ( start_grammar_weight - grammar_errors + 10) / 2)+ 0.5) / (Sulfur_Output_DeviceMobileORother_Percent * 3)
            else:
                grammar_placeholder = grammar_errors / (math.ceil(Sulfur_Output_Device_Desktop_Percent) + 1)
                Sulfur_Output_DeviceMobileORother_Percent += ((0.5 + grammar_placeholder / (grammar_placeholder) / 2) + 0.5) / (Sulfur_Output_DeviceMobileORother_Percent * 3)



        if Sulfur_Output_Device_Desktop_Percent == Sulfur_Output_DeviceMobileORother_Percent:
            Device_Result = "NOT_SET"
            with open(file_path_OutputData_name_Device, "w") as file:
                file.write("Not found")
        elif Sulfur_Output_Device_Desktop_Percent > Sulfur_Output_DeviceMobileORother_Percent:
            Device_Result = "DESKTOP"
            with open(file_path_OutputData_name_Device, "w") as file:
                file.write("Desktop")
        else:  # Sulfur_Output_Device_Desktop_Percent < Sulfur_Output_DeviceMobileORother_Percent
            Device_Result = "MOBILE(OTHER)"
            with open(file_path_OutputData_name_Device, "w") as file:
                file.write("Mobile (Other)")




        #ai.write_training_data(input_data, file_path_training_data, Device_Result) why is there 2 ai traning data scriptrs??? 8/3/2025


        return Device_Result, Device_Accuracy












    def summarise_device(self):
        file_path_OutputData_name_Device  = call.device()
        with open(file_path_OutputData_name_Device, "r") as file:
            OutputDevice = file.read().strip()
            return OutputDevice




    #add sck
    #add ml model



    def write_training_data(self, text, file_path, result):
        global Attribute_Device_Result
        conserve_space_random = random.randint(1,10)
        if conserve_space_random > 5:
            with open(file_path, "a", encoding="utf-8", errors="ignore") as file:
                random_int = random.randint(1, 10)
                if random_int >= 8:
                    file.write(f"{text} - UNSUPERVISED,")
                else:
                    text_v2 = []
                    capital_indices = [i for i, char in enumerate(str(text)) if
                                       char.isupper()]
                    capital_first_string = 0  # Default value

                    if isinstance(text, list) and len(text) > 0 and len(text[0]) > 0:
                        if text[0][0].isupper():
                            capital_first_string = 1
                        else:
                            capital_first_string = 0
                    else:
                        print("Error: text is not in the expected format.")



                    if capital_indices:
                        capitals_info = ', '.join(str(i) for i in capital_indices)
                        text_v2.append(f"{text} [CAPITALS = YES at indices: {capitals_info}]")
                    else: text_v2.append(f"{text} [CAPITALS = NO]")

                    if capital_first_string == 1: text_v2.append(f"[FIRST WORD CAPITAL = YES]")
                    else: text_v2.append(f"[FIRST WORD CAPITAL = NO")



                    global Device_Result
                    text_v2.append(f"[DEVICE : {result}]")
                    text_v2.append(f"[DEVICE_ACCURACY : {Device_Accuracy}]")


                    file.write(f"{''.join(text_v2)} - SUPERVISED ,")
        else:
            pass #50% chance to write actual training data











def call_file_input():
    global file_link
    file_link = file_path_input

def call_file_attributes():
    global file_link_a
    file_link_a = file_path_attributes

def call_file_output():
    global file_link_o
    file_link_o = file_path_output

def broadcast_verify(file):
    return os.path.exists(file)
class ai_process_cd():



    def process_script(self):
        if globals().get("__caller__") == "__main__":
            Sulfur.think("[This version is the standard release]")
            Sulfur.think("[Reading Data]")


        global total_time_ms,Device_Result

        ai_process_instance = ai_process_cd()

        if globals().get("__caller__") == "__main__":
            for i in tqdm(range(99), desc="Thinking", total=100):
                time.sleep(0.001)
        data_log = DataLog()
        data_log.check_input()
        sk = Sk()
        ai = Ai()
        global machine_model_checkDevice_result, machine_model_checkDevice_result_accuracy, accuracy
        ai.check_device()
        OutputDevice = ai.summarise_device()
        sk.label_write_sk_data()
        file_path_training_data = call.training_data()
        input_data,too_long,re_was_subbed = txt_data.verify_input("list")
        ai.write_training_data(input_data,file_path_training_data[2],Device_Result)
        if globals().get("__caller__") == "__main__":
            for i in tqdm(range(1), desc="Finishing", total=1):
                time.sleep(0.01)


        # Delayed import
        global Device_Accuracy,hours,minutes,seconds,total_time_ms
        # Write output
        return Device_Result, Device_Accuracy








def device_accuracy_export(accuracy):
    device_accuracy_export = accuracy
    return accuracy


