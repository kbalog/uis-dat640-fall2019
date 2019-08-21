# Assignment 1A: Spam Classification

**UPDATE 21/09 12:00** You will soon receive an email with your team ID, teammate (if applies), and link to your GitHub repository. In the meantime, you can find the two starer files here: [classifier.py](classifier.py) and [Report.md](Report.md).

**URGENT** sign up for the assignment using this form: https://forms.gle/jc3TbUXW2He4XeHv9.

## Scenario

You have been hired by a company as a data scientist, and you need to help build a spam classifier.  That is, create a model that is able to correctly classify the incoming emails to company email accounts as either spam or genuine non-spam ("ham") emails.

## Task

You are given a training dataset of over 82k emails, which are labeled either as spam or ham. Emails are stored as (ISO-8859-1 encoded) text files and organized in a set of folders (`train/XYZ`). The corresponding ground truth labels can be found in `train/labels.csv`.

Based on this data, your ultimate goal is to build a classifier that processes all emails under (`test/XYZ`), a total of over 9k documents, makes a ham/spam prediction for each, and outputs these in a similar CSV format.

The idea is to make this classification by assigning each email a spam score. Emails above a certain score threshold will be labeled as spam, otherwise regarded as ham. Figuring out how to compute the spam score and what is an appropriate threshold is your main task; this is where having labeled data will help you big time.

Your overall objective is to beat the baseline classifier (which labels everything with the majority class) by at least 10% in terms of Accuracy.

## Specific steps

#### 1) Download corpus

Download the email corpus from the [URL provided on Canvas](https://stavanger.instructure.com/courses/4586/discussion_topics/41462) and unzip it to a `data` folder.

#### 2) Split the labeled data

Split the labeled dataset (i.e., the one under `data/train`) into training and validation splits for development.  You may also split it k-fold for cross-validation.

NOTE: Below, we will simply assume that you copied part of the original `train` data as a training split to one folder (referred to as `train-data-dir`) and the remaining part as validation split to another folder (`validation-data-dir`).  If you want to be smarter about it and avoid physically copying (and effectively duplicating) the collection (possibly multiple times), then you're free to do something more elegant (e.g., just creating a list of filenames that belong to the training/validation splits). But this is entirely optional.

#### 3) Implement the spam classifier

Complete the missing parts of the `classifier.py` Python script.  

Train a model on the training split of your dataset by running:

```
python classifier.py -mode train --data {train-data-dir} --output {model-file}
```

Then apply your model on the validation split:

```
python classifier.py -mode predict --data {validation-data-dir} --model {model-file} --output {prediction-file}
```

  - The format and contents of the `model-file` is completely up to you. You probably want to collect some statistics from the training data, which you can then utilize when computing the spam score.
  - The `prediction-file` should be in csv format, with Id and Label fields, where Id is the file path relative to the `data` folder, e.g.:
  ```
  Id,Label
  train/000/001,spam
  train/000/007,spam
  train/000/009,spam
  ```

You can evaluate your classifier's performance using:

```
python classifier.py -mode eval --predictions {predictions-file} -- ground_truth {ground-truth-file}
```

Iterate these steps until you're satisfied with the model's performance.

#### 4) Upload predictions to Kaggle

Train a model using all labeled data and then apply it on the test data. Essentially, you want to run:

```
python classifier.py -mode train --data {prefix}/data/train --output {model-file}
python classifier.py -mode predict --data {prefix}/data/test --model {model-file} --output {prediction-file}
```

Then, upload the predictions file to Kaggle at: *[link-to-be-added]*.

Use "Team-XYZ (teamname)" as your team name. You are free to choose the text inside the brackets (as long as it is not offensive or inappropriate).

You can make at most one submission per day. Only the last submission counts, and it overwrites the previous ones.  You will see a "Baseline" entry on the leaderboard; this is what you want to beat by 10%.

#### 5) Write a report

Complete the `Report.md` under your team's GitHub repository.

#### 6) Commit and push changes

Hopefully, you've been committing and pushing changes along the way. Make sure that both the completed `classifier.py` and the `Report.md` files are there, by checking your repository on the web interface (https://github.com/uis-dat640-fall2019/1a-team-XYZ-handin). We'll fetch this repository when the deadline is due. You don't need to send us anything.

## Assignment scoring

The specific criteria for scoring the assignment is as follows: *to be added*.

## FAQ

  * **Is there a limitation to the techniques we are allowed to use? Should we use machine learning approaches?**
    - There is no limitation to what techniques you are allowed to use. But at this point there is no need for using advanced machine learning approaches. Instead, try to focus on simple heuristics and coding everything from ground up yourself.
  * **Why the one submission per day limit on Kaggle?**
    - Because we don't want you to train your model against the held-out test data. In a real-world setting, you would only have a single shot at applying the model on the training data. So we're actually being very generous here.
