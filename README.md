> # ⚠️ Preview versions are not stable. They are _not_ tested.
# SulfurAI-DRL-001-03-63
# Developer Release 1-03-63
## _Later releases may be in other repositories or in branches._
 
## WARNING:
### _This model is WORK IN PROGRESS, please report any NON-SECURITY issues to the said issues tab._


## What is SulfurAI?

_SulfurAI is a Local Analytical Model that anylyses text input to find user preference & info from a small dataset , designed to run in the background of an application or website._

## How do i use SulfurAI?

First, add your input to data/input.txt
Then run 
_Run SulfurAI.bat_

_Note: there is a 50 character limit and special characters will be removed._

## How is Sulfur trained?

_The current model uses the sulfax architecture, splitting data across 2 sets and further dividing the data with an 80/20 ratio._

_Data is labelled with 3 parameters:
 <input,accuracy,predicted device>_

 _This provides the model with a minimum 50% accuracy, which is planned to be scaled to 70% by 2026._

## SulfurAI's purpose.

_To find the preferences of a user base and average ratios efficiently, providing companies or regular users with insights on how to improve reach._


## Dependancies:
## _-Python with version 3.11_
_We cannot ensure Sulfur will run if it is not the correct version._

-Python Libraries:
 _Although Sulfur attempts to install all libraries, the following list is incase any fail:_
  ### Python NLTK
  _Provides word & sentiment analysis._
  ### Python TensorFlow 
  _Provides Neural Networking._
  ### Python TQDM,
  _Provides Loading GUI._
  ### Python PyTorch (Although not used.)
  _Will provide ML and CUDA integration._
  ### Python Pygame
  _Provides easy GUI._
  ### Python Sklearn
  _Provides machine learning processes._
  ### Python LanguageToolPython
  _Analyses Language for NLTK._
  ### Python Langdetect
  _Assists LanguageTool._
  ### Python Numpy
  _Handles datasets efficiently._
  ### Python Transformers
  _Provides GenAI and ML solutions._

## _-CUDA_
_While not necessary as of this version, Nvidia CUDA support will be needed for later releases._

## Thats all. Enjoy!
  
  

