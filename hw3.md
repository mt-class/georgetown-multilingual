---
layout: default
img: dalle1.png
img_link: http://www.statmt.org/book/
title: Homework 2: Multilingual NLP
img2: dalle2.png
img2_link: http://www.statmt.org/nmt-book/
active_tab: main_page
---

Linguistic Typology - DUE MARCH 27 11:59 PM
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


For the first part of this assignent, we are going to look at two features from WALS that many languages have:

* Look at feature 81A (Word Order)
* 69A (Tense-Aspect Suffixes)


```
Data is from WALS v2020.3 DOI: 10.5281/zenodo.7385533 

Dryer, Matthew S. & Haspelmath, Martin (eds.) 2013.
WALS Online (v2020.3) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.7385533
(Available online at https://wals.info, Accessed on 2024-02-21.)
```

The data is taken from WALS. Specifically located [here](https://github.com/cldf-datasets/wals/tree/master/cldf). I've taken values.csv and split it into a train and test set. Any language code that starts with a W, X, Y, or Z is in the test set. The rest is in the training set. Don't do this for anything actually related to science. This is a biased sample - however, there is no overlap between training and test.

Here are the data splits:
* [train](./hw3/train_langs.csv)
* [test](./hw3/test_langs.csv)
* [train feature values](./hw3/train_values_gold.csv)
* [test feature values](./hw3/test_values_gold.csv)

We will train a random forest classifier on this using scikit-learn.


Testing on our training set (overfitting) gives a score of 0.292. WALS has 255 possible language families, so randomly guessing would give a score just below 0.004. This means the model is learning something, but it cannot discern everything. Again this is overfitting on training. Evaluating on the heldout test set gives a score of 0.198. So this is still better than random. The Maximum Likelihood Estimate (just gussing the langauge family that occurs the most) would give a score of.

Select Your Own Features
=============================================================
Clearly, Word Order and Tense-Aspect Suffixes are only a subset of features of a language. Choose another feature that has broad coverage across language families. You can look for one with broad coverage just by browsing the WALS website.

A quick bash script to filter for classifier features is 
```
grep '^69A-' test_values_gold.csv | awk -F ',' '{printf "%s,%s\n", $2, $4}'
```

DELIVERABLES:
* Write which feature you chose and WHY  you think it will work (10 points)
* Run the same classifier but now with this third feature included. Report Training and test scores (10 points)
* Choose a second feature. Use this INSTEAD of your last feature - so that you still have 3. Write why you think it will work and report scores of train and test (20 points)


Use a different classifier than a random forest in scikit-learn
===============================================================
Random forests are not the only classifiers that are in Machine Learning. While they work very well, scikit-learn contains many other classifiers. For this next part,
choose a different classifier and repeat the steps above.

DELIVERABLES:
* Report scores for train and test on 81A and 69A (10 points)
* Report scores for train and test on 81A and 69A and your first new feature (10 points)
* Report scores for train and test on 81A and 69A and your second new feature (10 points)


Try and get above 0.500
==============================================================
The easiest way to get over 0.500 is to overfit by selecting too many features. However, this isn't great from a scientific, engineering, or linguistics perspective. Using the random forest classifier, try and get a score on test above 0.500 using the FEWEST number of features possible.

DELIVERABLES:
* Report scores on train and test for your list of features (10 points)
* List your features and explain why you think they help (10 points)
* Bonus points for the student who gets the fewest number of features to get above 0.500 in the class

Write-Up
========

Please write about 500 words on the assignment. Include disucssion about how and why features fail.
For instance, why would you think a feature would work but scores are not great. Also, explain why
you thought a feature would work, and then if it did, explain why.

DELIVERABLES:
* 500 word short answer (10 points)
