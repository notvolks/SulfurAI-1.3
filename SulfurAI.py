import os,subprocess,sys
from VersionDATA.ai_renderer import error
TOS = [
    "By using this application you agree to the Terms of Service listed in the project files.",
    "If you cannot find it, install a new version."
]
print_verti_list = error.print_verti_list
error_print = error.error
print_verti_list(TOS)

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


print("-------Preparing PIP libraries.")
def safe_import(module_name, package_name=None, extra_packages=None):
    try:
        __import__(module_name)
    except ImportError:
        pkg = package_name or module_name
        print(f"-------{pkg} not found. Installing...")
        install([pkg] + (extra_packages or []))
        try:
            __import__(module_name)
        except ImportError:
            print(f"Error while importing {module_name} after installation. Restart Sulfur to fix the bug.")

modules = [
    ("sklearn", "scikit-learn"),
    ("pygame", "pygame-ce"),
    ("pygame_gui",),
    ("language_tool_python",),
    ("langdetect",),
    ("tqdm",),
    ("numpy",),
    ("nltk",),
    ("pandas",),
    ("transformers",),
    ("torch", None, ["torchvision", "torchaudio"])
]

for mod in modules:
    safe_import(*mod)



print("-------All custom libraries are installed. ")

###########initiates the settings after install


import os
import sys
import subprocess
import random
import datetime
import time,math
from decimal import Decimal
from importlib.metadata import PackageNotFoundError
from VersionDATA.ai_renderer import Mean_device_s
from VersionDATA.ai_renderer import module_restore_trainingData
from VersionDATA.ai_renderer import preferences_basic_compare_s
from VersionDATA.ai_renderer_2 import sentence_detectAndInfer_s
from VersionDATA.verification.input_text import txt_data

module_restore_trainingData.restore_data()

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

# Global variables
global machine_model_checkDevice_result, machine_model_checkDevice_result_accuracy, accuracy
machine_model_checkDevice_result = 0
machine_model_checkDevice_result_accuracy = 0
accuracy = 0


# Global variables for device output
global Sulfur_Output_Device_Desktop_Percent, Sulfur_Output_DeviceMobileORother_Percent, OutputDevice, Device_Result
Device_Result = "NOT_SET"



def get_call_file_path():
    from VersionDATA.ai_renderer import call_file_path
    return call_file_path.Call()

# Call file paths
call = get_call_file_path()
file_path_OutputData_name_Device = call.device()  # Assume this returns a single path
(folder_path_OuputData, folder_path_OuputData_name_Device_accuracy, file_path_OutputData_name_Device_accuracy) = call.device_accuracy()
(folder_path_OuputData, folder_path_OuputData_name_Response_Time_MS, file_path_OutputData_name_Response_Time_MS) = call.response_time()
(folder_path_trainingData_grammar, folder_path_trainingData_grammar_name, file_path_trainingData_grammar) = call.grammar()
(folder_path_output, folder_path_output_name, file_path_output) = call.output()
(folder_path_archFullTimeRendererSulfax, folder_path_archFullTimeRendererSulfax_name, file_path_archFullTimeRendererSulfax) = call.arch()
(folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk) = call.training_data_sk()

class Arch:
    instant_shutdown = error.instant_shutdown

    def arch_items_append(self, item):
        global arch_items
        arch_items.append(item)

    @staticmethod
    def arch_items_extend(item):
        global arch_items
        arch_items.extend(item)

    def check_run(self):
        global lines_list, arch_items
        if "run = True" in lines_list and "run = True" in arch_items:
            pass
        if "run = False" in lines_list and "run = False" in arch_items:
            self.instant_shutdown("ARCH ERROR.NOT RAN. INSTALL NEW VER.")
        if "start_arch = True" in lines_list and "start_arch = True" in arch_items:
            pass
        if "start_arch = False" in lines_list and "start_arch = False" in arch_items:
            self.instant_shutdown("ARCH ERROR. NOT STARTED. INSTALL NEW VER.")

    def check_lines(self):
        call = get_call_file_path()
        global lines_list, arch_items
        arch_items = ["run = True", "run = False", "start_arch = True", "start_arch = False"]
        folder_path_colon_symbol, folder_path_colon_symbol_name, file_path_colon_symbol = call.arch_colon()
        with open(file_path_colon_symbol, "r") as file:
            lines = file.readlines()
            colon_data = ', '.join(lines)
            if "{" in colon_data:
                self.arch_items_append("{")
            if "}" in colon_data:
                self.arch_items_append("}")

        global folder_path_archFullTimeRendererSulfax, folder_path_archFullTimeRendererSulfax_name, file_path_archFullTimeRendererSulfax
        with open(file_path_archFullTimeRendererSulfax, "r") as file:
            lines_list = [line.strip() for line in file.readlines()]
            self.check_run()

    def verify_input(self):
        file_path_text_data_verify = call.text_data_verify()
        if os.path.exists(file_path_text_data_verify):
            pass
        else:
            error_print("er2", "Verification_input", "INSTALL NEW VER", 12)
            self.instant_shutdown("VERIFY ERROR. NOT STARTED. INSTALL NEW VER. [input-data_vrfy]")

arch = Arch()
arch.check_lines()
arch.verify_input()

def variable_call():
    version = "[DRL]"
    file_link = ""
    file_link_a = ""
    file_link_o = ""
    Sulfur_Output_Device_Desktop_Percent = 0
    Sulfur_Output_DeviceMobileORother_Percent = 0
    return version, file_link, file_link_a, file_link_o, Sulfur_Output_Device_Desktop_Percent, Sulfur_Output_DeviceMobileORother_Percent

version, file_link, file_link_a, file_link_o, Sulfur_Output_Device_Desktop_Percent, Sulfur_Output_DeviceMobileORother_Percent = variable_call()




def call_ai_class(class_name):
    if class_name == "CD":
        from VersionDATA.ai_renderer import Check_device_s  # Delayed import
        return Check_device_s

brick_out = error.brick_out


def finish_script():
    global start_time, file_path_OutputData_name_Response_Time_MS
    global hours, minutes, seconds, total_time_ms
    finish_time = datetime.datetime.now()
    finish_time_printed = finish_time.strftime("%Y-%m-%d %H:%M:%S") + f".{finish_time.microsecond // 1000:03d}"
    print(f"-------All tasks completed at {finish_time_printed}. Check output file.")
    total_time = finish_time - start_time
    total_time_ms = total_time.total_seconds() * 1000
    total_seconds = int(total_time.total_seconds())
    if total_time_ms > 1000:
        repeat_ttms = math.floor(total_time_ms / 1000)
        for x in range(repeat_ttms):
            total_time_ms -= 1000
            total_seconds += 1
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"-------Time taken: {hours} hours, {minutes} minutes, {seconds} seconds, {total_time_ms} milliseconds.")
    with open(file_path_OutputData_name_Response_Time_MS, "w") as file:
        file.write(f"{hours} hours, {minutes} minutes, {seconds} seconds, {total_time_ms} milliseconds.")



def rest_of_the_script():


    # Write output
    Check_device_s = call_ai_class("CD")
    instance = Check_device_s.Ai()
    ai_process_cd_instance = Check_device_s.ai_process_cd()
    Device_Result, Device_Accuracy = ai_process_cd_instance.process_script()




    global hours,minutes,seconds,total_time_ms

    finish_script()
    try:
        preferences_input = []
        current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__),))
        folder_path_input = os.path.join(current_dir_i, 'DATA')
        file_name_input = 'Input.txt'  # Debugger variables
        file_name_attributes = "Attributes.txt"
        file_name_output = "Output.txt"
        file_path_input = os.path.join(folder_path_input, file_name_input)
        file_path_attributes = os.path.join(folder_path_input, file_name_attributes)
        file_path_output = os.path.join(folder_path_input, file_name_output)
        instance_preferences = preferences_basic_compare_s.prefer_compare()
        #only using one script to be efficient
        wanted_noun_most_important_user, wanted_noun_most_important_global, preferences_user, preferences_text_global, wanted_verb_most_important_user, wanted_verb_most_important_global, input_data, adjective_describe_user, adjective_describe_global, mood_user, mood_global, mood_accuracy_user, mood_accuracy_global,average_mood_accuracy = instance_preferences.get_process(3) # set to 3 for basic model!
        stype_user, sintent_user,acc_sent_user,acc_intent_user,avg_sent_types,avg_intent_types,acc_sent_global,acc_intent_global,avg_accuracy_global = sentence_detectAndInfer_s.sentence_intent_and_infer()




        #ai functions
        OutputDevice = instance.summarise_device()
        main_devices = Mean_device_s.get_main_device()
        average_accuracy = Mean_device_s.get_main_accuracy()
        input_data, too_long,re_was_subbed = txt_data.verify_input("list")


        with open(file_path_output, "w", encoding="utf-8", errors="ignore") as file:

            file.write(f"###########Sulfur Output:###########*\n")
            file.write(f"---------------INPUT---------------\n")
            file.write(f"                                   \n")
            file.write(f"Input (text) : {input_data}\n")
            if too_long: file.write(f"Input Error : Input is too long. Stripped to below cap.\n")
            if re_was_subbed: file.write(f"-Certain unaccepted parts of the input may be removed. \n")
            if re_was_subbed: file.write(f"-This could affect output. \n")
            file.write(f"                                   \n")
            file.write(f"---------------DEVICES---------------\n")
            file.write(f"                                   \n")
            file.write(f"*Predicted using Machine Learning.*\n")
            file.write(f" Predicted Device : {OutputDevice}\n")
            file.write(f" Predicted Device Accuracy : {Device_Accuracy}%\n")
            file.write(f" Main/Mean Devices : {main_devices}\n")
            file.write(f" Average/Mean Accuracy: {average_accuracy}%\n")
            file.write(f"                                   \n")
            file.write(f"---------------PREFERENCES---------------\n")
            file.write("###########The basic version has a limit of 3 preferred words. To upgrade look for a newer version or switch to a possible business version.###########\n")
            preferred_words = ",".join(preferences_user)
            file.write(f"*Predicted using Hard Values.*\n")
            file.write(f" User(s) most important words (preferred) : {preferred_words} [Not Summarised]\n")
            file.write(f" Average/Mean important words (preferred) : {preferences_text_global} [Not Summarised]\n")
            file.write(f"                                   \n")
            file.write( " ###########Nouns###########:\n")
            file.write(f"  User(s) want (preferred) : {wanted_noun_most_important_user} [Can be plural (To an extent of noun)]\n")
            file.write(f"  Average/Mean want (preferred) : {wanted_noun_most_important_global} [Can be plural (To an extent of noun)]\n")
            file.write(f"                                   \n")
            file.write(" ###########Verbs###########:\n")
            file.write(f"  User(s) are doing (preferred) : {wanted_verb_most_important_user} [Can be  plural/singular (To an extent of verb)]\n")
            file.write(f"  Average/Mean are doing (preferred) : {wanted_verb_most_important_global} [Can be plural/singular (To an extent of verb)]\n")
            file.write(f"                                   \n")
            file.write(" ###########Adjectives###########:\n")
            file.write(f"  User(s) are describing (preferred) : {adjective_describe_user} [Can be  plural/singular (To an extent of adjective)]\n")
            file.write(f"  Average/Mean are describing (preferred) : {adjective_describe_global} [Can be plural/singular (To an extent of adjective)]\n")
            file.write(f"                                   \n")
            file.write(" ###########Mood###########:\n")
            file.write(f"  User(s) are (emotion) : {mood_user} [(To an extent of emotion)]\n")
            file.write(f"  Average/Mean are (emotion) : {mood_global} [(To an extent of emotion)]\n")
            file.write(f"                                   \n")
            file.write(f"  Predicted User Mood Accuracy : {mood_accuracy_user}%\n")
            file.write(f"  Average/Mean Mood Accuracy : {mood_accuracy_global}%\n")
            file.write(f"  Average <User : Mean> Accuracy : {average_mood_accuracy}%\n")
            file.write(" ###########Sentence Analysis###########:\n")
            file.write(f"*Predicted using a Neural Network.*\n")
            file.write(f"  Predicted user sentence type : {stype_user}\n")
            file.write(f"  Predicted user sentence type accuracy : {acc_sent_user * 100}%\n")
            file.write(f"                                   \n")
            file.write(f"  Predicted user sentence intent : {sintent_user}\n")
            file.write(f"  Predicted user sentence intent accuracy : {acc_intent_user * 100}%\n")
            file.write(f"                                   \n")
            file.write(f"  Predicted global sentence type : {avg_sent_types}\n")
            file.write(f"  Predicted global sentence type accuracy : {acc_sent_global * 100}%\n")
            file.write(f"                                   \n")
            file.write(f"  Predicted global sentence intent : {avg_intent_types}\n")
            file.write(f"  Predicted global sentence intent accuracy : {acc_intent_global * 100}%\n")
            file.write(f"                                   \n")
            file.write(f"  Predicted global intent + sentence accuracy : {avg_accuracy_global * 100}%\n")
            file.write(f"                                   \n")
            file.write(f"---------------RESPONSE---------------\n")
            file.write(f"Response Time : {str(f'{hours} hours, {minutes} minutes, {seconds} seconds, {total_time_ms} milliseconds.')}\n")
            file.write(
                "###########This file is only used for general debugging, to access the individual output variables, use the API or the output_data folder.###########\n")
            file.write(f"                                   \n")
            file.write(f"*SulfurAI can make mistakes. Check important info.\n")
    except IOError as e:
        print(f"Error writing output: {e}")

    time.sleep(100)  # Only used for developer debug

# Menu & Variables
list_menu = [
    f"#####Sulfur AI {version}#####",
    "####A VolksHub production####",
    "....Booting Nodes...."
]  # Menu
start_time = datetime.datetime.now()
start_time_printed = start_time.strftime(
    "%Y-%m-%d %H:%M:%S")  # Calculating what it starts at for rest_of_the_script(attributes)
start_time_ms = f".{start_time.microsecond // 1000:03d}"
print_verti_list(list_menu)
rest_of_the_script()


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

# Debugger
if not os.path.exists(folder_path_input):  # Checks if it can be verified
    error_print("er1", "DEPENDANCY_FILE", "VERIFY",1)
else:
    with open(file_path_verify, 'r') as file:
        lines = file.readlines()
        if lines:
            first_line = lines[0].strip()
            if first_line != "os1_tvt":
                error_print("er2", "Verification", "INSTALL NEW VER",1)
                brick_out(1000)

# Check for input, attributes, and output files


