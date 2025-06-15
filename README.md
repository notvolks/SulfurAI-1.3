<div align="center">

![image alt](https://github.com/notvolks/SulfurAI-1.3/blob/main/GitHub/images/sulfurai_txt.png?raw=true)

`SulfurAI - your fully modifiable analytical agent.`

Developer Release 1-03-85-PREVIEW7

  <br />

<a href="https://github.com/topoteretes/cognee">
  <img src="https://github.com/notvolks/SulfurAI-1.3/blob/main/GitHub/images/sulfurai_desc.png?raw=true" alt="Cognee Logo" height="500">
</a>
  
 
## WARNING:
> ### _This model is WORK IN PROGRESS, please report any NON-SECURITY issues to the said issues tab._

## ❓ What is SulfurAI ❓

> _SulfurAI is a Local Analytical Model that anylyses text input to find user preference & info from a small dataset , designed to run in the background of an application or website._

## 🤔 How do i use SulfurAI 🤔

### _----------------------------Simple python running----------------------------_

<div align="left">
  
> First, add your input to DATA/input.txt
>, then open the file:
> 
 `Run SulfurAI.bat`

> **Note:** There is a character limit, and special characters will be removed. You can change these settings in the configuration.

---

<div align="center">

### _-------------------------------- Using the API --------------------------------_

</div>

<div align="left">


### _🐍 Python: Local 🐍_

1. **Create a new script** in the root SulfurAI folder. This will be your initialization script.

2. Add the following lines of code:

   ```python
   import SulfurAI
   SulfurAI.setup_local()
   ```

3. Run the script and then add any code from the documentation as a return.

4. You can create your own script or use an existing one in any directory, importing this initialization script with your required returns.

<div align="center">

---

> For more in-depth information, see the API folder.

---

## 🔨 How is Sulfur trained 🔨

> _The current model uses the sulfax architecture, splitting data across 4 sets and further dividing the data with an 80/20 [labelled/un-labelled] ratio._

```
Data is labelled with 3 parameters:
 <input,accuracy,predicted device>

 This provides the model with a minimum 50% accuracy, which is planned to be scaled to 70% by 2026.
```

## SulfurAI's purpose.

> _To find the preferences of a user base and average ratios efficiently, providing companies or regular users with insights on how to improve reach and retention._

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

  --Python Langcodes--
  Provides Location conversion.




-CUDA-
While not necessary as of this version, Nvidia CUDA support will be needed for later releases.
```

We are committed to making open source an enjoyable and respectful experience for our community. See <a href="https://github.com/notvolks/SulfurAI-1.3/blob/7659173774ff6fc09db1a1a957fa08d0f45bfea8/CODE_OF_CONDUCT.md"><code>CODE_OF_CONDUCT</code></a> for more information.

## 💬 Other FAQ 💬

---

> _Do I need to restart my system after Sulfur installs?_
> 
> _Answer: No, sulfur does *not* require a system restart after installation, although it may require a manual restart._

---

> _Does Sulfur encrypt my cache/training data?_
> 
> _Answer: No, Sulfur does *not* encrypt cache/training_data as it is designed to run locally. Server support and encryption will be available on the business version._

---

> _Can I create my own model with Sulfur?_
> 
> _Answer: Yes, you can modify every Sulfur script to make your own model, full support for this will come in later updates with user friendly UI._

---

`Send more questions to: nb.volkshub.inquiries@gmail.com`

---

## 💫 Contributors

<a href="https://github.com/notvolks/SulfurAI-1.3/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=notvolks/SulfurAI-1.3" />
</a>
