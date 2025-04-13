
import re,os
too_long_id = False

def get_call_file_path():
    from DATA.ai_renderer import call_file_path
    return call_file_path.Call()

# Call file paths
call = get_call_file_path()


class Ensure():
    def __init__(self,max_length=50): #modify this via settings?
        self.max_length = max_length


    def strip_input(self,input):

        input_text = input.strip()
        input_text = re.sub(r"[\'\";\\&<>%^\s,]+", "", input_text)
        if not input_text:
            raise ValueError("Invalid username: empty after cleaning.")
        return input_text

    def strip_input_list(self, input_list):

        input_list_text = input_list.strip()
        input_list_text = re.sub(r"[\'\";\\&<>%^,]+", "", input_list_text)
        if not input_list_text:
            raise ValueError("Invalid username: empty after cleaning.")
        return [input_list_text]

    def clear_length_list(self,input_list_text):
        too_long = False
        if len(",".join(input_list_text)) > self.max_length:
            input_list_text = input_list_text[:self.max_length]
            too_long = True
        return too_long,input_list_text

    def clear_length(self, input_list_text):
        too_long = False
        if len(",".join(input_list_text)) > self.max_length:
            input_list_text = input_list_text[:self.max_length]
            too_long = True
        return too_long, input_list_text


def call_ensure():
    return Ensure()

def verify_input(string_or_list):
    user_data_verified = ""
    too_long_id_list = False
    too_long_id = False
    too_long = False
    user_data_input = ""
    current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..'))
    folder_path_input = os.path.join(current_dir_i, 'DATA')
    file_name_input = 'Input.txt'
    file_path_input = os.path.join(folder_path_input, file_name_input)
    with open(file_path_input, 'r', encoding='utf-8', errors='ignore') as file:  input_data = [line.strip() for line in file.readlines() if line.strip()]

    ensure = call_ensure()
    if string_or_list.lower() == "string":
        user_data_input = ensure.strip_input(",".join(input_data))
        too_long, user_data_verified = ensure.clear_length(user_data_input)
    elif string_or_list.lower() == "list":
        user_data_input = ensure.strip_input_list(",".join(input_data))
        too_long, user_data_verified = ensure.clear_length_list(user_data_input)


    return user_data_verified,too_long

