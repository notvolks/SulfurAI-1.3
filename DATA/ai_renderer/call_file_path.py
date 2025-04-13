import os

class Call():

    def device(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        # Define the expected folder path for Output_Data
        folder_path_OutputData = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OutputData_name_Device = "Device.txt"

        # Construct the full path to Device.txt
        file_path_OutputData_name_Device = os.path.join(folder_path_OutputData, folder_path_OutputData_name_Device)
        return  file_path_OutputData_name_Device

    def device_accuracy(self):

        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_Device_accuracy = "Device_Accuracy.txt"
        file_path_OutputData_name_Device_accuracy = os.path.join(folder_path_OuputData, folder_path_OuputData_name_Device_accuracy)
        return folder_path_OuputData, folder_path_OuputData_name_Device_accuracy, file_path_OutputData_name_Device_accuracy

    def mean_device(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_mean_device = "Main_Device.txt"
        file_path_OutputData_name_mean_device = os.path.join(folder_path_OuputData,
                                                                 folder_path_OuputData_name_mean_device)
        return  file_path_OutputData_name_mean_device

    def average_device_accuracy(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_mean_device_average_device_accuracy = "Average_accuracy.txt"
        file_path_OutputData_name_mean_device_average_device_accuracy = os.path.join(folder_path_OuputData,
                                                             folder_path_OuputData_name_mean_device_average_device_accuracy)
        return file_path_OutputData_name_mean_device_average_device_accuracy

    def response_time(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_Response_Time_MS = "Response_Time_MS.txt"
        file_path_OutputData_name_Response_Time_MS = os.path.join(folder_path_OuputData, folder_path_OuputData_name_Response_Time_MS)
        return folder_path_OuputData, folder_path_OuputData_name_Response_Time_MS, file_path_OutputData_name_Response_Time_MS


    def grammar(self):
        folder_path_trainingData_grammar = os.path.join(os.path.dirname(os.path.abspath(__file__)),'DATA/training_data/grammar_func=checkdevice')
        folder_path_trainingData_grammar_name = "RepositlessGrammar.txt"
        file_path_trainingData_grammar = os.path.join(folder_path_trainingData_grammar,folder_path_trainingData_grammar_name)
        return folder_path_trainingData_grammar,folder_path_trainingData_grammar_name,file_path_trainingData_grammar

    def output(self):
        folder_path_output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DATA')
        folder_path_output_name = ("Output.txt")
        file_path_output = os.path.join(folder_path_output, folder_path_output_name)
        return folder_path_output,folder_path_output_name,file_path_output

    def arch(self):
        global folder_path_archFullTimeRendererSulfax,folder_path_archFullTimeRendererSulfax_name,file_path_archFullTimeRendererSulfax
        folder_path_archFullTimeRendererSulfax = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Sulfax-Architechture/build 001-01')
        folder_path_archFullTimeRendererSulfax_name = ("archFullTimeRendererSulfax.txt")
        file_path_archFullTimeRendererSulfax = os.path.join(folder_path_archFullTimeRendererSulfax,folder_path_archFullTimeRendererSulfax_name)
        return folder_path_archFullTimeRendererSulfax,folder_path_archFullTimeRendererSulfax_name,file_path_archFullTimeRendererSulfax

    def arch_colon(self):
        global folder_path_colon_symbol, folder_path_colon_symbol, file_path_colon_symbol
        folder_path_colon_symbol = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Sulfax-Architechture/build 001-01')
        folder_path_colon_symbol_name = ("colon-symbol.txt")
        file_path_colon_symbol = os.path.join(folder_path_colon_symbol, folder_path_colon_symbol_name)
        return folder_path_colon_symbol, folder_path_colon_symbol_name, file_path_colon_symbol

    def training_data(self):
        global folder_path_training_data,folder_path_training_data_name,file_path_training_data
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ))
        folder_path_training_data = os.path.join(current_dir,"DATA", 'training_data', "data_train")
        #folder_path_training_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'DATA/training_data/data_train')
        folder_path_training_data_name = ("data.txt")
        file_path_training_data = os.path.join(folder_path_training_data, folder_path_training_data_name)
        return folder_path_training_data,folder_path_training_data_name,file_path_training_data

    def training_data_sk(self):
        global folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ))
        folder_path_training_data_sk = os.path.join(current_dir, "DATA", 'training_data', "data_train_sk")
        #folder_path_training_data_sk = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 #'DATA/training_data/data_train_sk')
        folder_path_training_data_name_sk = ("data.txt")
        file_path_training_data_sk = os.path.join(folder_path_training_data_sk, folder_path_training_data_name_sk)
        return folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk

    def backup_training_data_sk(self):
        global folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ))
        folder_path_training_data_sk_backup = os.path.join(current_dir, "DATA", 'training_data', "BACKUP-DO-NOT-DELETE", "backup_sk")
        # folder_path_training_data_sk = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        # 'DATA/training_data/data_train_sk')
        folder_path_training_data_name_sk_backup = ("data.txt")
        file_path_training_data_sk_backup = os.path.join(folder_path_training_data_sk_backup, folder_path_training_data_name_sk_backup)
        return file_path_training_data_sk_backup

    def backup_training_data(self):
        global folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ))
        folder_path_training_data_backup = os.path.join(current_dir, "DATA", 'training_data', "BACKUP-DO-NOT-DELETE", "backup_normal")
        # folder_path_training_data_sk = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        # 'DATA/training_data/data_train_sk')
        folder_path_training_data_name_backup = ("data.txt")
        file_path_training_data_backup = os.path.join(folder_path_training_data_backup, folder_path_training_data_name_backup)
        return file_path_training_data_backup

    def settings_extra_debug(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_settings = os.path.join(current_dir, 'DATA', 'Settings')
        folder_path_settings_name_extra_debug = "extra_debug.txt"
        file_path_settings_name_extra_device = os.path.join(folder_path_settings,
                                                             folder_path_settings_name_extra_debug)
        return file_path_settings_name_extra_device

    def settings_backup(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_settings = os.path.join(current_dir, 'DATA', 'Settings')
        folder_path_settings_name_backup = "backup_valid.txt"
        file_path_settings_name_backup = os.path.join(folder_path_settings,
                                                            folder_path_settings_name_backup)
        return file_path_settings_name_backup

    def preferences_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_preferences_user = "Preferences_user.txt"
        file_path_OutputData_name_preferences_user = os.path.join(folder_path_OuputData,
                                                             folder_path_OuputData_name_preferences_user)
        return file_path_OutputData_name_preferences_user

    def preferences_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_name_preferences_global = "Preferences_global.txt"
        file_path_OutputData_name_preferences_global = os.path.join(folder_path_OuputData,
                                                             folder_path_OuputData_name_preferences_global)
        return file_path_OutputData_name_preferences_global

    def Wanted_noun_most_important_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Wanted_noun_most_important_global = "Wanted_noun_most_important_global.txt"
        file_path_OutputData_Wanted_noun_most_important_global = os.path.join(folder_path_OuputData,
                                                             folder_path_OuputData_Wanted_noun_most_important_global)
        return file_path_OutputData_Wanted_noun_most_important_global

    def Wanted_noun_most_important_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Wanted_noun_most_important_user = "Wanted_noun_most_important_user.txt"
        file_path_OutputData_Wanted_noun_most_important_user = os.path.join(folder_path_OuputData,
                                                             folder_path_OuputData_Wanted_noun_most_important_user)
        return file_path_OutputData_Wanted_noun_most_important_user

    def Wanted_verb_most_important_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Wanted_verb_most_important_global = "Wanted_verb_most_important_global.txt"
        file_path_OutputData_Wanted_verb_most_important_global = os.path.join(folder_path_OuputData,
                                                                              folder_path_OuputData_Wanted_verb_most_important_global)
        return file_path_OutputData_Wanted_verb_most_important_global

    def Wanted_verb_most_important_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Wanted_verb_most_important_user = "Wanted_verb_most_important_user.txt"
        file_path_OutputData_Wanted_verb_most_important_user = os.path.join(folder_path_OuputData,
                                                                            folder_path_OuputData_Wanted_verb_most_important_user)
        return file_path_OutputData_Wanted_verb_most_important_user

    def Describe_adjective_most_important_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Describe_adjective_most_important_global = "Describe_adjective_global.txt"
        file_path_OutputData_Describe_adjective_most_important_global = os.path.join(folder_path_OuputData,
                                                                              folder_path_OuputData_Describe_adjective_most_important_global)
        return file_path_OutputData_Describe_adjective_most_important_global

    def Describe_adjective_most_important_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_Describe_adjective_user = "Describe_adjective_user.txt"
        file_path_OutputData_Describe_adjective_user = os.path.join(folder_path_OuputData,
                                                                            folder_path_OuputData_Describe_adjective_user)
        return file_path_OutputData_Describe_adjective_user

    def mood_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_mood_user = "Preferences_Mood_User.txt"
        file_path_OutputData_mood_user = os.path.join(folder_path_OuputData,
                                                                            folder_path_OuputData_mood_user)
        return file_path_OutputData_mood_user

    def mood_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_mood_global = "Preferences_Mood_Global.txt"
        file_path_OutputData_mood_global = os.path.join(folder_path_OuputData,
                                                      folder_path_OuputData_mood_global)
        return file_path_OutputData_mood_global

    def mood_accuracy_user(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_mood_accuracy = "Preferences_Mood_Accuracy_User.txt"
        file_path_OutputData_mood_accuracy_user = os.path.join(folder_path_OuputData,
                                                      folder_path_OuputData_mood_accuracy)
        return file_path_OutputData_mood_accuracy_user

    def mood_accuracy_global(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_OuputData_average_device_accuracy = os.path.join(current_dir, 'DATA', 'Output_Data')
        folder_path_OuputData_mood_accuracy = "Preferences_Mood_Accuracy_Global.txt"
        file_path_OutputData_mood_accuracy_global = os.path.join(folder_path_OuputData,
                                                               folder_path_OuputData_mood_accuracy)
        return file_path_OutputData_mood_accuracy_global

    def text_data_verify(self):
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        folder_path_verify = os.path.join(current_dir, 'DATA', 'verification',"input_text")
        folder_path_text_data_verify = "txt_data.py"
        file_path_text_data_verify = os.path.join(folder_path_verify,
                                                                 folder_path_text_data_verify)
        return file_path_text_data_verify

call = Call()
file_path_OutputData_name_Device  = call.device()
folder_path_OuputData, folder_path_OuputData_name_Device_accuracy, file_path_OutputData_name_Device_accuracy = call.device_accuracy()
folder_path_OuputData, folder_path_OuputData_name_Response_Time_MS, file_path_OutputData_name_Response_Time_MS = call.response_time()
folder_path_trainingData_grammar,folder_path_trainingData_grammar_name,file_path_trainingData_grammar = call.grammar()
folder_path_output,folder_path_output_name,file_path_output = call.output()
folder_path_archFullTimeRendererSulfax,folder_path_archFullTimeRendererSulfax_name,file_path_archFullTimeRendererSulfax = call.arch()
folder_path_training_data_sk, folder_path_training_data_name_sk, file_path_training_data_sk = call.training_data_sk()