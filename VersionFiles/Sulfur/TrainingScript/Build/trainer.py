import os,subprocess,sys
import importlib,random
from contextlib import contextmanager

##########debugitems

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
    pkg = package_name or module_name

    while automatic_restart_failsafe < 3:  # retry limit,add in settings, list of scripts with this in it: sulfur, trainer,
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
                      f"Attempt {automatic_restart_failsafe}/3. "
                      f"Restart Sulfur if this persists.")
                if automatic_restart_failsafe >= 3:
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
    ("faker", "faker"),
    ("tensorflow",),
]

for mod in modules:
    safe_import(*mod)



print("-------All custom libraries are installed. ")
from faker import Faker
import nltk
from nltk.corpus import names, wordnet as wn
try: nltk.data.find('corpora/names')
except LookupError: nltk.download('names', quiet=True)
try: nltk.data.find('corpora/wordnet')
except LookupError: nltk.download('wordnet', quiet=True)



##########################LogicItems

fake = Faker()


def generate_sentence(style):
    verb = ""
    subject = random.choice(names.words())

    ########SubLogicItems

    def get_compatible_verbs(noun):
        noun_synsets = wn.synsets(noun, pos=wn.NOUN)
        compatible_verbs = []

        for synset in noun_synsets:
            for lemma in synset.lemmas():
                derivs = lemma.derivationally_related_forms()
                for d in derivs:
                    if d.synset().pos() == 'v':
                        compatible_verbs.append(d.name())

        return list(set(compatible_verbs))

    def add_complementary_elements(verb, obj):

        adjectives = [adj.name().split('.')[0] for adj in wn.all_synsets('a') if len(adj.name().split('.')[0]) <= 8]
        obj_adj = random.choice(adjectives) if random.random() > 0.5 else ""


        adverbs = [adv.name().split('.')[0] for adv in wn.all_synsets('r') if len(adv.name().split('.')[0]) <= 8]
        verb_adv = random.choice(adverbs) if random.random() > 0.5 else ""

        use_passive = random.random() > 0.7
        if use_passive:
            verb = f"was {verb} by"
        if obj_adj:
            obj = f"{obj_adj} {obj}"

        return verb, obj

    ########Actual Function

    objects = [n.name().split('.')[0] for n in wn.all_synsets('n') if len(n.name().split('.')[0]) <= 8]
    obj = random.choice(objects)

    if style == "premiumenglish":
        verbs = get_compatible_verbs(obj)
        verb = random.choice(verbs) if verbs else "did"
        verb, obj = add_complementary_elements(verb, obj)
    elif style == "natural":
        verbs = [v.name().split('.')[0] for v in wn.all_synsets('v') if len(v.name().split('.')[0]) <= 8]
        verb = random.choice(verbs)

    prefix_options = [
        "",
        "Yesterday, ",
        f"On {fake.day_of_week()}, ",
        f"This morning at {fake.time(pattern='%H:%M')}, ",
    ]
    prefix = random.choice(prefix_options)

    sentence = f"{prefix}{subject} {verb} the {obj}."
    return sentence.capitalize()




########################MenuItems




id_run_train = 0
call = get_call_file_path()

file_path_autotrainer_debug = call.settings_auto_trainer_extra_debug()


with open(file_path_autotrainer_debug, "r", encoding="utf-8", errors="ignore") as file:  extra_debug_autotrainer = file.readlines()
########Menu
print("Presenting Menu.....")
print("--------------------Select the trainer methods.--------------------")

print("######SentenceGenerationType######")
print("- Legacy: Provides basic sentences that are quick and easy to process. Not recommended for large datasets.")
print("- Natural: Provides more complex and coherent sentences that are good for large datasets. (BETA)")
print("- PremiumEnglish: Provides ultra coherent sentences that have in-depth context. Good for large context models/features but is extremely slow. (BETA)")
while True:
    legacy_options = input("Select the sentence generation type:").strip().lower()
    if legacy_options == "natural" or legacy_options == "legacy" or legacy_options == "premiumenglish": break
    print("Must select 'Legacy' , 'Natural' or 'PremiumEnglish'.")


########ScriptRunner
while True:
    id_run_train += 1
    print(f"######################---------Running Trainer on loop **{id_run_train}**")
    if str(extra_debug_autotrainer) == "yes": print(f"###################--------- SulfurAI is starting...")

    if str(extra_debug_autotrainer) == "yes": print(f"################--------- SulfurAI is generating a sentence...")
    match legacy_options:
        case "legacy":  sentence = fake.sentence()
        case "natural":  sentence = str(generate_sentence("natural"))
        case "premiumenglish": sentence = str(generate_sentence("premiumenglish"))
        case _: sentence = fake.sentence()
    if str(extra_debug_autotrainer) == "yes": print(f"################--------- SulfurAI generated a sentence...")


    current_dir_i = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..','..',))
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..','..', ))
    folder_path_input = os.path.join(current_dir_i, 'DATA')
    file_name_input = 'Input.txt'  # Debugger variables
    file_path_input = os.path.join(folder_path_input, file_name_input)
    with open(file_path_input, "w", encoding="utf-8", errors="ignore") as file: file.write(str(sentence))
    try:
        if str(extra_debug_autotrainer) == "yes": print(f"###################--------- SulfurAI is processing...")
        subprocess.run(
            [sys.executable, 'SulfurAI.py'],
            cwd=current_dir,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running SulfurAI.py: {e}")
    if str(extra_debug_autotrainer) == "yes": print(f"###################--------- SulfurAI finished processing.")

