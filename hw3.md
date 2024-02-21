---
layout: default
img: dalle1.png
img_link: http://www.statmt.org/book/
title: Homework 2: Multilingual NLP
img2: dalle2.png
img2_link: http://www.statmt.org/nmt-book/
active_tab: main_page
---

Linguistic Typology - DUE MARCH 6 11:59 PM
=========================================================
This assignment looks at trying to use varying machine learning techniques to classify languages together. Specificaly, we will look at linguistic features of languages to predict how they should be grouped together.

Scikit-learn
---------------------------------------------------------
We will be using the machine learning toolkit scikit-learn. This is a python package that implements many different ML algorithms.

To install, I recommend using a conda enviornment. If you do not have this installed already, you can [get the software here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). It is probably best to use the regular installation, but miniconda will likely work as well.

After you have conda installed, you can either use the graphical interface that it has for some operating systems, or use a command line approach. The following commands should get you everything you need for this assignment:

```
conda create --name wals python=3.8
conda activate wals
pip install scikit-learn # Make sure you are in your conda environment (previous command) before running this!
python -c "import sklearn; sklearn.show_versions()" # Check that it is installed 1.3.2
pip install pandas
```

You can learn more about scikit-learn from [the official website](https://scikit-learn.org/stable/getting_started.html#fitting-and-predicting-estimator-basics).

WALS
-------------------------------------------------------------
We will be using the [World Atlas of Language Structures (WALS)](https://wals.info) for this assignment. It has thousands of languages with various linguistic features annotated with references to linguistic publications. We will use various features of this to try and predict language family.

Look at feature 81A (Word Order)
69A Tense-Aspect Suffixes


```
Data is from WALS v2020.3 DOI: 10.5281/zenodo.7385533 

Dryer, Matthew S. & Haspelmath, Martin (eds.) 2013.
WALS Online (v2020.3) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.7385533
(Available online at https://wals.info, Accessed on 2024-02-21.)
```