import os,subprocess,sys,importlib
from VersionDATA.ai_renderer import error
TOS = [
    "By using this application you agree to the Terms of Service listed in the project files.",
    "If you cannot find it, install a new version."
]
print_verti_list = error.print_verti_list
error_print = error.error
print_verti_list(TOS)

def get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()

# Call file paths
call = get_call_file_path()

def install(packages):
    """
    Custom install function for handling package installation with special cases like pygame-ce.
    """
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


def get_installed_packages():
    """
    Retrieve all installed packages and their top-level modules.
    Dynamically creates a module-to-package mapping.
    """
    package_map = {}
    for dist in importlib.metadata.distributions():
        try:
            # Get the package name
            package_name = dist.metadata["Name"]
            # Get the top-level modules provided by the package
            top_level = dist.read_text("top_level.txt")
            if top_level:
                for module in top_level.splitlines():
                    package_map[module] = package_name
        except KeyError:
            # Skip packages without proper metadata
            pass
    return package_map


print("-------Preparing PIP libraries.")
def safe_import(module_name, package_name=None, extra_packages=None):
    MODULE_TO_PACKAGE_MAP = {
        "sklearn": "scikit-learn",
        "pygame": "pygame-ce",
        "torchvision": "torchvision",
        "torchaudio": "torchaudio",
        "beautifulsoup4": "bs4",
    }
    automatic_restart_failsafe = 0
    file_path_pip_py_restart_limit = call.settings_pip_fallback_amount()
    with open(file_path_pip_py_restart_limit, "r", encoding="utf-8", errors="ignore") as file: automatic_restart_limit = str(file.readline())
    pkg = package_name or module_name

    while automatic_restart_failsafe < int(automatic_restart_limit):
        try:

            return importlib.import_module(module_name)
        except ImportError:
            print(f"------- {pkg} not found. Installing...")

            install([pkg] + (extra_packages or []))

            try:
                module_name_printed = module_name
                if module_name in MODULE_TO_PACKAGE_MAP: module_name_printed = MODULE_TO_PACKAGE_MAP[module_name]
                return importlib.import_module(module_name_printed)
            except ImportError:
                automatic_restart_failsafe += 1
                print(f"Error while importing {module_name} after installation. "
                      f"Attempt {automatic_restart_failsafe}/{automatic_restart_limit}. "
                      f"Restart Sulfur if this persists.")
                if automatic_restart_failsafe >= int(automatic_restart_limit):
                    print(f"Failed to import {module_name} after multiple attempts. This could be a fake error - check previous print statements to ensure.")
                    return None

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
    ("torch", None, ["torchvision", "torchaudio"]),
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
from VersionDATA.ai_renderer_2 import sentence_detectAndCompare_s
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



file_path_OutputData_name_Device = call.device()  # Assume this returns a single path
(folder_path_OuputData, folder_path_OuputData_name_Device_accuracy, file_path_OutputData_name_Device_accuracy) = call.device_accuracy()
(folder_path_OuputData, folder_path_OuputData_name_Response_Time_MS, file_path_OutputData_name_Response_Time_MS) = call.response_time()
(folder_path_trainingData_grammar, folder_path_trainingData_grammar_name, file_path_trainingData_grammar) = call.grammar()
(folder_path_output, folder_path_output_name, file_path_output) = call.output()
(folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk) = call.training_data_sk()

####################Architechture:
ARCH_IS_VALID = 0
file_path_arch = call.arch_runner()
folder_path_arch = call.arch_runner_folder()
if os.path.exists(file_path_arch): ARCH_IS_VALID += 1
if os.path.exists(folder_path_arch): ARCH_IS_VALID += 1
##########define ARCHITECTURE
def start_arch():
    arch = arch_runner.Arch()
    arch.check_lines()
    arch.verify_input()

##########run ARCHITECTURE

if ARCH_IS_VALID == 2:
    try:
        from VersionFiles.Sulfur.ArchitectureBuild import arch_runner
        start_arch()
    except (ImportError,AttributeError,TypeError,FileNotFoundError,ValueError) as e:
        print(f"ARCHITECTURE COULD NOT BE RUN! Error as {e}")
        print("Shutting down sulfur...")
        time.sleep(2)
        error.brick_out(2)

else:
    try:
        print("ARCHITECTURE COULD NOT BE VERIFIED!")
        print("Shutting down sulfur...")
        time.sleep(2)
        error.brick_out(2)
    except (ImportError,TypeError,AttributeError,KeyboardInterrupt) as e:
        print(f"ARCHITECTURE COULD NOT BE CLOSED ('ARCHITECTURE COULD NOT BE VERIFIED' RAN INTO AN ERROR)! Error as {e}")
        print("Shutting down sulfur...")
        time.sleep(2)
        error.brick_out(2)



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

def ui_add_output_data(file_path,changes,changes_summary,average_summary,changes_apart,item,item_least):
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        file.write(f" ###########{item} Changes###########:\n")
        file.write(f" Changes to your userbase over the past {changes} {item_least}:\n")
        file.write("  " + f"{changes_summary}\n" if changes_summary else "  " + f"None_Found\n")
        file.write(f" Average Changes to your userbase over the past {changes} {item_least}:\n")
        file.write("  " + f"{average_summary}\n" if average_summary else "  " + f"None_Found\n")
        file.write(f" *Only includes userbase changes at least {changes_apart} {item_least} apart.\n")


def rest_of_the_script():
    # Write output
    Check_device_s = call_ai_class("CD")
    instance = Check_device_s.Ai()
    ai_process_cd_instance = Check_device_s.ai_process_cd()
    Device_Result, Device_Accuracy = ai_process_cd_instance.process_script()

    global hours, minutes, seconds, total_time_ms

    finish_script()
    try:
        # === Load Input and Preferences ===
        preferences_input = []
        current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        folder_path_input = os.path.join(current_dir_i, 'DATA')
        file_name_input = 'Input.txt'
        file_name_attributes = "Attributes.txt"
        file_name_output = "Output.txt"

        file_path_input = os.path.join(folder_path_input, file_name_input)
        file_path_attributes = os.path.join(folder_path_input, file_name_attributes)
        file_path_output = os.path.join(folder_path_input, file_name_output)

        instance_preferences = preferences_basic_compare_s.prefer_compare()
        (
            wanted_noun_most_important_user, wanted_noun_most_important_global, preferences_user,
            preferences_text_global, wanted_verb_most_important_user, wanted_verb_most_important_global,
            input_data, adjective_describe_user, adjective_describe_global, mood_user, mood_global,
            mood_accuracy_user, mood_accuracy_global, average_mood_accuracy
        ) = instance_preferences.get_process(3)

        (
            stype_user, sintent_user, acc_sent_user, acc_intent_user,
            avg_sent_types, avg_intent_types, acc_sent_global, acc_intent_global, avg_accuracy_global
        ) = sentence_detectAndInfer_s.sentence_intent_and_infer()

        # === Read Time-Based Change Settings ===
        file_path_settings_name_ui_days_ago = call.settings_ui_days_ago()
        file_path_settings_name_ui_days_apart = call.settings_ui_days_apart()
        file_path_settings_name_ui_weeks_ago = call.settings_ui_weeks_ago()
        file_path_settings_name_ui_weeks_apart = call.settings_ui_weeks_apart()
        file_path_settings_name_ui_months_ago = call.settings_ui_months_ago()
        file_path_settings_name_ui_months_apart = call.settings_ui_months_apart()
        file_path_settings_name_ui_years_ago = call.settings_ui_years_ago()
        file_path_settings_name_ui_years_apart = call.settings_ui_years_apart()

        with open(file_path_settings_name_ui_days_ago, "r", encoding="utf-8", errors="ignore") as f:
            past_d_changes = int(f.readline())
        with open(file_path_settings_name_ui_days_apart, "r", encoding="utf-8", errors="ignore") as f:
            changes_d_apart_at_leastDays = int(f.readline())

        with open(file_path_settings_name_ui_weeks_ago, "r", encoding="utf-8", errors="ignore") as f:
            past_w_changes = int(f.readline())
        with open(file_path_settings_name_ui_weeks_apart, "r", encoding="utf-8", errors="ignore") as f:
            changes_w_apart_at_leastWeek = int(f.readline())

        with open(file_path_settings_name_ui_months_ago, "r", encoding="utf-8", errors="ignore") as f:
            past_m_changes = int(f.readline())
        with open(file_path_settings_name_ui_months_apart, "r", encoding="utf-8", errors="ignore") as f:
            changes_m_apart_at_leastMonth = int(f.readline())

        with open(file_path_settings_name_ui_years_ago, "r", encoding="utf-8", errors="ignore") as f:
            past_y_changes = int(f.readline())
        with open(file_path_settings_name_ui_years_apart, "r", encoding="utf-8", errors="ignore") as f:
            changes_y_apart_at_leastYear = int(f.readline())

        # === Detect Changes ===
        changes_summary_day, average_change_d = sentence_detectAndCompare_s.run_model(past_d_changes, changes_d_apart_at_leastDays, "day")
        changes_summary_week, average_change_w = sentence_detectAndCompare_s.run_model(past_w_changes, changes_w_apart_at_leastWeek, "week")
        changes_summary_month, average_change_m = sentence_detectAndCompare_s.run_model(past_m_changes, changes_m_apart_at_leastMonth, "month")
        changes_summary_year, average_change_y = sentence_detectAndCompare_s.run_model(past_y_changes, changes_y_apart_at_leastYear, "year")

        # === UI Output Data ===
        ui_add_output_data(call.ui_day_changes(), past_d_changes, changes_summary_day, average_change_d, changes_d_apart_at_leastDays, "Day", "days")
        ui_add_output_data(call.ui_week_changes(), past_w_changes, changes_summary_week, average_change_w, changes_w_apart_at_leastWeek, "Week", "weeks")
        ui_add_output_data(call.ui_month_changes(), past_m_changes, changes_summary_month, average_change_m, changes_m_apart_at_leastMonth, "Month", "months")
        ui_add_output_data(call.ui_year_changes(), past_y_changes, changes_summary_year, average_change_y, changes_y_apart_at_leastYear, "Year", "years")

        # === AI Device and Input Verification ===
        OutputDevice = instance.summarise_device()
        main_devices = Mean_device_s.get_main_device()
        average_accuracy = Mean_device_s.get_main_accuracy()
        input_data, too_long, re_was_subbed = txt_data.verify_input("list")

        # === Output Writer Function ===

        max_lines = 12 #add settings for

        def write_userbase_changes(file, label, past_range, summary, avg, apart_unit, bypass_limit):
            def truncate_lines(text):
                if not text:
                    return "None_Found"
                lines = text.splitlines()
                if len(lines) > max_lines:
                    return '\n'.join(lines[:max_lines]) + f"\n...and {len(lines) - max_lines} more lines. Removed due to limit cap."
                return text
            file.write(f" ###########{label} Changes###########:\n")
            file.write(f" Changes to your userbase over the past {past_range} {label.lower()}s:\n")
            if bypass_limit:
                file.write("  " + (summary if summary else "None_Found") + "\n")
            else:
                file.write("  " + truncate_lines(summary) + "\n")

            file.write(f" Average Changes over the past {past_range} {label.lower()}s:\n")

            if bypass_limit:
                file.write("  " + (avg if avg else "None_Found") + "\n")
            else:
                file.write("  " + truncate_lines(avg) + "\n")

            file.write(f" *Only includes changes at least {apart_unit} {label.lower()}s apart.\n\n")

        # === Write Output to File ===
        try:
            with open(file_path_output, "w", encoding="utf-8", errors="ignore") as file:
                file.write("###########Sulfur Output:###########*\n")
                file.write("---------------INPUT---------------\n\n")
                file.write(f"Input (text) : {input_data}\n")
                if too_long:
                    file.write("Input Error : Input is too long. Stripped to below cap.\n")
                if re_was_subbed:
                    file.write("-Certain unaccepted parts of the input may be removed.\n")
                    file.write("-This could affect output.\n")

                file.write("\n---------------DEVICES---------------\n\n")
                file.write("*Predicted using Machine Learning.*\n")
                file.write(f" Predicted Device : {OutputDevice}\n")
                file.write(f" Predicted Device Accuracy : {Device_Accuracy}%\n")
                file.write(f" Main/Mean Devices : {main_devices}\n")
                file.write(f" Average/Mean Accuracy: {average_accuracy}%\n")

                file.write("\n---------------PREFERENCES---------------\n")
                file.write("###########Basic version limit: 3 preferred words###########\n")
                file.write("*Predicted using Hard Values.*\n")
                file.write(f" User(s) preferred words : {','.join(preferences_user)} [Not Summarised]\n")
                file.write(f" Average preferred words : {preferences_text_global} [Not Summarised]\n\n")

                def section(title, user, global_val, extra=""):
                    file.write(f" ###########{title}###########:\n")
                    file.write(f"  User(s): {user} {extra}\n")
                    file.write(f"  Average: {global_val} {extra}\n\n")

                section("Nouns", wanted_noun_most_important_user, wanted_noun_most_important_global, "[To an extent of noun]")
                section("Verbs", wanted_verb_most_important_user, wanted_verb_most_important_global, "[To an extent of verb]")
                section("Adjectives", adjective_describe_user, adjective_describe_global, "[To an extent of adjective]")
                section("Mood", mood_user, mood_global, "[To an extent of emotion]")

                file.write(f"  Predicted Mood Accuracy : {mood_accuracy_user}% (user), {mood_accuracy_global}% (global)\n")
                file.write(f"  Average <User : Mean> Accuracy : {average_mood_accuracy}%\n")
                file.write("*Predicted using a Neural Network.*\n")
                file.write(f"  Sentence Type : {stype_user} ({acc_sent_user * 100}%)\n")
                file.write(f"  Sentence Intent : {sintent_user} ({acc_intent_user * 100}%)\n")
                file.write(f"  Global Type : {avg_sent_types} ({acc_sent_global * 100}%)\n")
                file.write(f"  Global Intent : {avg_intent_types} ({acc_intent_global * 100}%)\n")
                file.write(f"  Overall Accuracy : {avg_accuracy_global * 100}%\n")

                file.write("---------------USER INSIGHT---------------\n")
                write_userbase_changes(file, "Day", past_d_changes, changes_summary_day, average_change_d, changes_d_apart_at_leastDays,False)
                write_userbase_changes(file, "Week", past_w_changes, changes_summary_week, average_change_w, changes_w_apart_at_leastWeek,False)
                write_userbase_changes(file, "Month", past_m_changes, changes_summary_month, average_change_m, changes_m_apart_at_leastMonth,False)
                write_userbase_changes(file, "Year", past_y_changes, changes_summary_year, average_change_y, changes_y_apart_at_leastYear,False)

                file.write("---------------RESPONSE---------------\n")
                file.write(f"Response Time : {hours}h {minutes}m {seconds}s, {total_time_ms}ms\n")
                file.write("###########General debugging only.###########\n")
                file.write("*Settings can be changed. SulfurAI may make mistakes.*\n")

                # === Optional Extra Output ===
                file_path_ui_extra_output_settings = call.settings_ui_write_to_seperate_output()
                with open(file_path_ui_extra_output_settings, "r", encoding="utf-8", errors="ignore") as file_extra:
                    ui_extra_output = file_extra.readline().strip()


                file_path_extra_output = call.Output_UserInsight()
                if ui_extra_output == "yes":
                    with open(file_path_extra_output, "w", encoding="utf-8", errors="ignore") as file:
                        file.write("--------------USER INSIGHT---------------\n")
                        write_userbase_changes(file, "Day", past_d_changes, changes_summary_day, average_change_d, changes_d_apart_at_leastDays,True)
                        write_userbase_changes(file, "Week", past_w_changes, changes_summary_week, average_change_w, changes_w_apart_at_leastWeek,True)
                        write_userbase_changes(file, "Month", past_m_changes, changes_summary_month, average_change_m, changes_m_apart_at_leastMonth,True)
                        write_userbase_changes(file, "Year", past_y_changes, changes_summary_year, average_change_y, changes_y_apart_at_leastYear,True)


        except IOError as e:
            print(f"Error writing output: {e}")

        time.sleep(100)  # Developer debug only

    except Exception as e:
        print(f"Unhandled exception during script run: {e}")



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
if __name__ == "__main__":
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


