# Assignment 1B: Advanced Spam Classification

## Task

Continuing from Assignment 1A, you have the same dataset and the purpose of your model is to correctly classify emails as either 'ham' or 'spam'.

However, in Assignment 1B your task is to use machine learning algorithms to train different classifiers on the training data, primarily using words as features.
Additionally, you will need to develop some other (non-term-frequency-based) features.

## Specific steps

#### 1) Standard features and algorithms

  * Three different term-weighting representations of the email body text must be used to train classifiers:  Term Count, Term Frequency (TF), and Term Frequency-Inverse Document Frequency (TF-IDF).
  * Two different machine learning algorithms must be used to train classifiers: Naive Bayes (`sklearn.naive_bayes.MultinomialNB`) and Support Vector Machines (`sklearn.svm.LinearSVC`).
  * For each of the six (2 x 3) possible combinations of standard text representation and algorithms, train a classifier and report the results on a validation split (similarly to Assignment 1A).

#### 2) Experimental approaches

  * Develop alternative features to train the classifier with in combination with the standard features.
  * You may also use other machine learning algorithms.
  * In the report, explain your choices both in terms of feature extraction and machine learning algorithms, and include the results of the different experimental approaches.
  * You must develop, test, and describe at least three experimental approaches in the report (that differ in one or more of (i) text pre-processing applied, (ii) set of features, (iii) choice of machine learning algorithm).

###### 2.1) Text pre-processing

  * The text in the datafiles will need to be pre-processed in order to train the classifiers. Exactly how this is done is up to you, but the finalized set of text pre-processing steps and the reasoning behind them need to be explained in the report.

###### 2.2) Develop new features

  * Develop at least three features which are not based on term frequencies in any way, and use these features when training your experimental approaches.  

#### 3) Submit your best model's predictions on Kaggle

  * Submit your best model's predictions on the test set to this assignment's Kaggle competition: https://www.kaggle.com/t/e05e60e385d64a93a26f0440cc08f06c
  * The portion of your grade for this assignment that is based on numerical performance will be based on this (see below).

#### 4) Write a report

Complete the `Report.md` under your team's GitHub repository.

#### 5) Commit and push changes

Hopefully, you've been committing and pushing changes along the way. Make sure that both the completed `classifier.py` and the `Report.md` files are there, by checking your repository on the web interface (https://github.com/uis-dat640-fall2019/1b-team-XYZ-handin). We'll fetch this repository when the deadline is due. You don't need to send us anything.

## Assignment scoring

The specific criteria for scoring the assignment is as follows:

  * Standard features and algorithms (5 points)
  * Text pre-processing and other extra steps (5 points)
  * Experimental approaches (5 points)
  * Accuracy, as measured by the Kaggle competition (computed by `floor(accuracy * 100)`):
      * 98%: 5 point
      * 97%: 4 points
      * 96%: 3 points
      * 95%: 2 points
      * 93%: 1 points

## Submission deadline

The deadline for submitting the report and code on GitHub is **16/09 17:00**.


## FAQ

  * **Why the one submission per day limit on Kaggle?**
    - Because we don't want you to train your model against the held-out test data. In a real-world setting, you would only have a single shot at applying the model on the training data. So we're actually being very generous here.
