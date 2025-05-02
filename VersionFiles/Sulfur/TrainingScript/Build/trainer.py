import os,subprocess,sys
import importlib
from contextlib import contextmanager


TOS = [
    "By using this application you agree to the Terms of Service listed in the project files.",
    "If you cannot find it, install a new version."
]
def print_verti_list(list):
    for item in list: print(item)
print_verti_list(TOS)

@contextmanager              # for future silencing of output
def suppress_output():
    with open(os.devnull, 'w') as f:
        old_stdout = sys.stdout
        sys.stdout = f
        try:
            yield
        finally:
            sys.stdout = old_stdout

def get_call_file_path():
    import call_file_path
    return call_file_path.Call()
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
    ("torch", None, ["torchvision", "torchaudio"]),
    ("faker", "faker"),
    ("tensorflow",),
]

for mod in modules:
    safe_import(*mod)



print("-------All custom libraries are installed. ")
from faker import Faker

id_run_train = 0
call = get_call_file_path()
########Menu
print("Presenting Menu.....")
print("--------------------Select the trainer methods.--------------------")

print("######SentenceGenerationType######")
print("- Legacy: Provides basic sentences that are quick and easy to process. Not recommended for large datasets.")
print("- Natural: Provides more complex sentences that are good for large datasets. (BETA)")
while True:
    legacy_options = input("Select the sentence generation type:").lower()
    if legacy_options == "natural" or legacy_options == "legacy": break
    print("Must select 'Natural' or 'Legacy'.")


########ScriptRunner
while True:
    id_run_train += 1
    print(f"######################---------Running Trainer on loop {id_run_train}")
    print(f"###################--------- SulfurAI is starting...")
    fake = Faker()
    sentence = ""
    if legacy_options == "legacy": sentence = fake.sentence()
    elif legacy_options == "natural": sentence = f"{fake.catch_phrase()} {fake.sentence()}"

    current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..',))
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..','..', ))
    folder_path_input = os.path.join(current_dir_i, 'DATA')
    file_name_input = 'Input.txt'  # Debugger variables
    file_path_input = os.path.join(folder_path_input, file_name_input)
    with open(file_path_input, "w", encoding="utf-8", errors="ignore") as file: file.write(str(sentence))
    try:
        print(f"###################--------- SulfurAI is processing...")
        subprocess.run(
            [sys.executable, 'SulfurAI.py'],
            cwd=current_dir,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running SulfurAI.py: {e}")
    print(f"###################--------- SulfurAI finished processing.")

