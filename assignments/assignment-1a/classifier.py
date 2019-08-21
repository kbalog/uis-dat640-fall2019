"""
DAT640 - Assignment 1

This is the template for the code part of your submission for Assignment 1.
"""

import argparse
import json
import os
import sys
from sklearn import metrics
import csv

LOG_LEVEL = 0  # Set to 1 for verbose mode


class EmailClassifier:

    def train(self, root_dir, datafiles_list):
        # We assume the ground truth labels are available
        labels_file = os.path.join(root_dir, 'labels.csv')
        if not os.path.isfile(labels_file):
            raise FileNotFoundError("labels.csv cannot be found in {}".format(root_dir))
        labels = load_labels(labels_file)

        # Process all data files
        for df in datafiles_list:
            # TODO: process data file
            filename = os.path.join(root_dir, df)
            label = labels.get(df, None)
            # Note: relative file path to root_dir is the document Id
            if LOG_LEVEL == 1:
                print("{} - {}".format(df, label))

        print("Training finished ({} training instances)".format(len(datafiles_list)))

    def predict(self, filename):
        """Make a prediction for a given document."""
        # TODO: implement a model that doesn't always return spam
        return 'spam'

    def predict_set(self, root_dir, datafiles_list, output_file):
        """Makes predictions for a set of documents in a given dir."""
        print("Making predictions for {} and writing them to {}".format(root_dir, output_file))
        with open(output_file, 'w') as f:
            f.write("Id,Label\n")
            for df in datafiles_list:
                # TODO: process data file
                filename = os.path.join(root_dir, df)
                label = self.predict(filename)
                f.write("{},{}\n".format(df, label))
                if LOG_LEVEL == 1:
                    print("{} - {}".format(df, label))

    def save(self, output_file):
        with open(output_file, 'w') as f:
            # TODO: implement model saving
            f.write('dummy')
        print("Model saved to {}".format(output_file))

    def load(self, model_path):
        print("Loading model from {}".format(model_path))
        # TODO: implement model loading
        pass


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', '-mode', default='predict',
                        choices=['predict', 'eval', 'train'],
                        help='Run script in a specific mode.')
    parser.add_argument('--data', help='Directory path to the data.')
    parser.add_argument('--model', help='File path from which to load a trained model.')
    parser.add_argument('--output', help='File path to save the file produced by this script.')
    parser.add_argument('--predictions', help='File path to the saved predictions for evaluation.')
    parser.add_argument('--ground_truth', help='File path to the ground truth file.')
    return parser


def load_labels(labels_file):
    """Load Id and Label pairs from a csv file and return them as a dictionary."""
    labels = dict()
    with open(labels_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            labels[row[0]] = row[1]
    return labels


def load_datafile_list(root_dir):
    """Load a list of data file paths in {root_dir}/xxx/yyy format."""
    datafiles_list = []
    subdirs_list = [x[0] for x in os.walk(root_dir)]
    if len(subdirs_list) > 0:
        for subdir in sorted(subdirs_list)[1:]:
            # Keep the upper two folder names as prefix to the filename
            prefix = "/".join(subdir.split("/")[-2:])
            for _, _, files in os.walk(subdir):
                for name in sorted(files):
                    datafiles_list.append("/".join([prefix, name]))
    return datafiles_list


def digitize_label(label):
    if label == 'spam':
        return 1
    elif label == 'ham':
        return 0
    return None


def evaluate_predictions(ground_path, preds_path):
    """Evaluate predictions against a ground truth file."""

    # Load predictions from file into a dictionary
    predictions = dict()
    with open(preds_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            id, label = row[0], digitize_label(row[1])
            predictions[id] = label

    # Evaluate predictions against the ground truth
    y_true = []
    y_pred = []
    with open(ground_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            id, label = row[0], digitize_label(row[1])
            if id not in predictions:
                raise KeyError("Missing prediction for document {}".format(id))
            y_true.append(label)
            y_pred.append(predictions[id])

    print("Evaluation results:")
    print("-------------------")
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
    print("Accuracy:            {:05.3f}".format((tp + tn) / (tp + tn + fp + fn)))
    print("Precision:           {:05.3f}".format(tp / (tp + fp)))
    print("False positive rate: {:05.3f}".format(fp / (fp + tn)))


if __name__ == "__main__":
    parser = argument_parser()
    args = parser.parse_args()
    datafiles_list = None
    data_path = None
    model_path = None
    preds_path = None
    ground_path = None

    # Check if dataset, model, predictions, or ground truth file are present:
    mode = args.__dict__['mode']
    if args.__dict__['data'] is not None:
        data_path = str(args.__dict__['data'])
        datafiles_list = load_datafile_list(data_path)

    if mode == 'train':
        model_path = str(args.__dict__['output'])
        ground_path = os.path.join(str(args.__dict__['data']), 'labels.csv')
    elif mode == 'predict':
        model_path = str(args.__dict__['model'])
        preds_path = str(args.__dict__['output'])
    elif mode == 'eval':
        preds_path = str(args.__dict__['predictions'])
        ground_path = str(args.__dict__['ground_truth'])

    # Check if provided paths/files exist
    if model_path and mode == 'predict':
        if not os.path.isfile(model_path):
            raise argparse.ArgumentTypeError("Invalid path: {}".format(model_path))
    if preds_path and mode == 'eval':
        if not os.path.isfile(preds_path):
            raise argparse.ArgumentTypeError("Invalid path: {}".format(preds_path))
    if ground_path:
        if not os.path.isfile(ground_path):
            raise argparse.ArgumentTypeError("Invalid path: {}".format(ground_path))

    if mode == 'train' and model_path:
        model = EmailClassifier()
        model.train(data_path, datafiles_list)
        model.save(model_path)
    elif mode == 'predict' and preds_path:
        model = EmailClassifier()
        model.load(model_path)
        model.predict_set(data_path, datafiles_list, preds_path)
    elif mode == 'eval':
        evaluate_predictions(ground_path, preds_path)
    else:
        print("Request not understood (invalid mode). Exiting.")
        sys.exit()
