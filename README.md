> # ⚠️ Preview versions are not stable. They are _not_ tested.
# SulfurAI-DRL-001-03-85-PREV3
# Developer Release 1-03-85-PREV3
> ## _Later releases may be in other repositories or in branches._
 
## WARNING:
> ### _This model is WORK IN PROGRESS, please report any NON-SECURITY issues to the said issues tab._


## What is SulfurAI?

> _SulfurAI is a Local Analytical Model that anylyses text input to find user preference & info from a small dataset , designed to run in the background of an application or website._

## How do i use SulfurAI?

> > ### _Simple python running._
> First, add your input to data/input.txt
> 
> Then run :
 `Run SulfurAI.bat`
> 
> _Note: there is a 50 character limit and special characters will be removed._

>  _--------------API--------------_

> > ### _Python: Local._
> First, create a new script in the root SulfurAI folder.
> 
> This will be your init script. Then add these lines of code :
> 
 `import SulfurAI`
>
 `SulfurAI.setup_local()`
 
> Afterwards, run the script and then add any script from the documentation as a return.
> Create your own script or use an existing one in any directory and import this init script, with your required returns.
>
>  _Note: It may install pip dependancies automatically or print statements. To stop this add a quiet loop around it._


## How is Sulfur trained?

> _The current model uses the sulfax architecture, splitting data across 2 sets and further dividing the data with an 80/20 ratio._
```
Data is labelled with 3 parameters:
 <input,accuracy,predicted device>

 This provides the model with a minimum 50% accuracy, which is planned to be scaled to 70% by 2026.
```
## SulfurAI's purpose.

> _To find the preferences of a user base and average ratios efficiently, providing companies or regular users with insights on how to improve reach._


## Dependancies:
```
-Python with version 3.11-
We cannot ensure Sulfur will run if it is not the correct version.

-Python Libraries:
 Although Sulfur attempts to install all libraries, the following list is incase any fail and must be installed manually:

  --Python NLTK--
  Provides word & sentiment analysis.

  --Python TensorFlow--
  Provides Neural Networking.

  --Python TQDM--
  Provides Loading GUI.

  --Python PyTorch (Although not used.)--
  Will provide ML and CUDA integration.

  --Python Pygame--
  Provides easy GUI.

  --Python Sklearn--
  Provides machine learning processes.

  --Python LanguageToolPython--
  Analyses Language for NLTK.

  --Python Langdetect--
  Assists LanguageTool.

  --Python Numpy--
  Handles datasets efficiently.

  --Python Transformers--
  Provides GenAI and ML solutions.

  --Python Fakers--
  Provides sentence generation.

  --Python Fasttext-wheel--
  Provides Location insight.

  --Python Pycountry--
  Provides Location insight.




-CUDA-
While not necessary as of this version, Nvidia CUDA support will be needed for later releases.
```
## Thats all. Enjoy!
  
  

