################ Welcome to SulfurAI dashboard installer!
### Functions here should be modified with proper intent.
### This python script was written in the Holly format. To find out how it works go into VersionDATA/HollyFormat/ReadMe.txt
### This python script is designed to install the SulfurAI dashboard and its dependencies.

### LAYOUT:
# ---------------GOING DOWN!
######- Calling files
#######-Installing packages

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





import time,subprocess,sys

try:
    import importlib
except ModuleNotFoundError: print("Module importlib not found. Due to the conditions, it cannot automatically be installed. Please install it using pip.")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def _get_call_file_path():
    from VersionFiles.Sulfur.TrainingScript.Build import call_file_path
    return call_file_path.Call()



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


call = _get_call_file_path()


def _upgrade_pip_tools():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        print("Warning: Failed to upgrade pip tools.")


def _install(packages):
    if isinstance(packages, str):
        packages = [packages]
    _upgrade_pip_tools()
    for pkg in packages:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pkg],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            print(f"Failed to install {pkg}.")

# Safe import with install retry
def _safe_import(module_name, package_name=None, extra_packages=None):
    """
    Tries to import a module, and if it fails, attempts to install the corresponding package
    (with optional extras), then import again, retrying up to a configured limit.
    """
    MODULE_TO_PACKAGE_MAP = {
        "sklearn": "scikit-learn",
        "pygame": "pygame-ce",
        "torchvision": "torchvision",
        "torchaudio": "torchaudio",
        "beautifulsoup4": "bs4",
    }

    automatic_restart_failsafe = 0
    file_path_pip_py_restart_limit = call.settings_pip_fallback_amount()  # Assumes this returns a file path with number
    with open(file_path_pip_py_restart_limit, "r", encoding="utf-8", errors="ignore") as file:
        automatic_restart_limit = int(file.readline().strip())

    pkg = package_name or MODULE_TO_PACKAGE_MAP.get(module_name, module_name)
    file_path_cache_localHost_pip_debug = call.cache_LocalpipCacheDebug()
    with open(file_path_cache_localHost_pip_debug, "r", encoding="utf-8", errors="ignore") as file: cache_stored_pip_debug = file.readlines()

    if module_name not in [line.strip() for line in cache_stored_pip_debug]:
        while automatic_restart_failsafe < automatic_restart_limit:
            try:
                return importlib.import_module(module_name)
            except ImportError:
                if __name__ == "__main__":
                    print(f"------- {pkg} not found. Installing...")
                _install([pkg] + (extra_packages or []))

                try:
                    return importlib.import_module(module_name)
                except ImportError:

                    automatic_restart_failsafe += 1
                    if __name__ == "__main__":
                        print(f"Error while importing {module_name} after installation. "
                              f"Attempt {automatic_restart_failsafe}/{automatic_restart_limit}. "
                              f"Restart Installer if this persists.")
                    if automatic_restart_failsafe >= automatic_restart_limit:
                        if __name__ == "__main__":
                            print(f"Failed to import {module_name} after multiple attempts. "
                                  f"This could be a fake error - check previous print statements.")
                            with open(file_path_cache_localHost_pip_debug, "a", encoding="utf-8", errors="ignore") as file: file.write(f"{module_name}\n")
                        return None

# Ensure required packages
modules = ["streamlit", "dash", "pandas", "plotly","pywebview"]
for mod in modules:
    _safe_import(mod)


time.sleep(100)