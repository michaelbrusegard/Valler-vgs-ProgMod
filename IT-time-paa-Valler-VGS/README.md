Machine Learning Notebooks
==========================


# Prerequisite

When using Anaconda, you can optionally create an isolated Python environment dedicated to this project. This is recommended as it makes it possible to have a different environment for each project (e.g. one for this project), with potentially different libraries and library versions:

$ conda create -n mlbook python=3.5 anaconda

$ conda activate mlbook


This creates a fresh Python 3.5 environment called mlbook (you can change the name if you want to), and it activates it. This environment contains all the scientific libraries that come with Anaconda. This includes all the libraries we will need (NumPy, Matplotlib, Pandas, Jupyter and a few others), except for TensorFlow, so let's install it:

$ conda install -n mlbook -c conda-forge tensorflow

$ conda install -n mlbook -c conda-forge  keras

$ conda install -n mlbook -c conda-forge scikit-learn


This installs the latest version of TensorFlow available for Anaconda (which is usually not the latest TensorFlow version) in the mlbook environment (fetching it from the conda-forge repository). If you chose not to create an mlbook environment, then just remove the -n mlbook option.

Next, you can optionally install Jupyter extensions. These are useful to have nice tables of contents in the notebooks, but they are not required.

$ conda install -n mlbook -c conda-forge jupyter_contrib_nbextensions

You are all set! Next, jump to the Starting Jupyter section.

# Installation

This assumes you already have pip installed. if not you should search for pip on the nett and download and install that first. 


download the repo from github. 

open the folder with a terminal. 

run 
```unix
pip3 install --user --upgrade pip
```

After this 

```unix
 python -m pip install --upgrade --user -r requirements.txt
```

To start the notebooks and get started with coding

```unix
jupyter notebook
```
