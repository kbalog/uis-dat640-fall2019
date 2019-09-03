import os
import csv
import re
from sklearn import metrics

LOG_LEVEL = 0

class EmailClassifier:    
    hams = dict()
    spams = dict()
    
    def storeInlists(self, label, keywords):
        if label=='ham':
            for word in keywords:
                if word in self.hams:
                    self.hams[word]+=1
                else:
                    self.hams[word]=1
        else:
            for word in keywords:
                if word in self.spams:
                    self.spams[word]+=1
                else:
                    self.spams[word]=1

    def get_subject(self, mail):
        with open(mail, 'r', errors='ignore') as f:
            mail_text = f.read(None)
            subjects = re.findall(r'[Ss]ubject:([^\n]*)', mail_text)
            subject = subjects[0] if len(subjects)>0 else ''
            return self.clean_subject(subject)

    def clean_subject(self, subject):
        subject = str(subject.strip()).lower()
        subject = re.sub(r'\d*', '', subject)
        subject=' '.join(' '.join(subject.split('-')).split('_'))
        subject = re.sub(r'[^\w^\s]*', '', subject)
        subject_contents = [word for word in subject.split(" ") if len(word)>0]
        #remove stop words
        # key_words = [word for word in subject_contents if word not in load_stopwords('stopwords')]
        return subject_contents

    def save_model(self, output_file):
        with open(output_file, 'w') as f:
            dictionaries =[self.hams, self.spams]
            f.write(str(dictionaries))
            f.close()
        print("Model saved to {}".format(output_file))

    def load_model(self, model_path):
        print("Loading model from {}".format(model_path))
        with open(model_path, 'r', errors='ignore') as f:
            dictionaries = eval(f.read(None))
            self.hams.update(dictionaries[0])
            self.spams.update(dictionaries[1])

    def predict(self, filename):
        subject_key_words = self.get_subject(filename)
        spam_score = sum([self.spams.get(word,0) for word in subject_key_words] )
        ham_score = sum([self.hams.get(word,0) for word in subject_key_words] )
        overall_spam_score = spam_score/(ham_score+spam_score+1)
        return ('spam' if overall_spam_score>0.40 else 'ham')

    def predict_set(self, root_dir, datafiles_list, output_file):
        with open(output_file, 'w') as f:
            f.write("Id,Label\n")
            for df in datafiles_list:
                # TODO: process data file
                filename = os.path.join(root_dir, df)
                label = self.predict(filename)
                f.write("{},{}\n".format(df, label))
                if LOG_LEVEL == 1:
                    print("{} - {}".format(df, label))
        print("{} Predictions Done".format(len(datafiles_list)))

def train(self, root_dir, datafiles_list):
        # We assume the ground truth labels are available
        labels_file = os.path.join(root_dir, 'train/labels.csv')
        if not os.path.isfile(labels_file):
            raise FileNotFoundError("labels.csv cannot be found in {}".format(root_dir))
        labels = load_labels(labels_file)

        # Process all training data files
        for df in datafiles_list:
            filename = '/'.join([root_dir, df])
            label = labels.get(df, None)
            subject_contents = self.get_subject(filename)
            self.storeInlists(label, subject_contents)
            # Note: relative file path to root_dir is the document Id
            if LOG_LEVEL == 1:
                print("{} - {}".format(df, label))

        self.save_model('/'.join([root_dir, 'train/Train_Model.txt']))

        print("Training finished ({} training data)".format(len(datafiles_list)))

def load_datafile_list(root_dir):
    """Load a list of data file paths in {root_dir}/xxx/yyy format."""
    datafiles_list = []
    # subdirs_list = [x[0] for x in os.walk(root_dir)]
    subdirs_list = ["/".join(x[0].split("\\")) for x in os.walk(root_dir)]
    if len(subdirs_list) > 0:
        for subdir in sorted(subdirs_list)[1:]:
            prefix = "/".join(subdir.split("/")[-2:])
            for _, _, files in os.walk(subdir):
                for name in sorted(files):
                    datafiles_list.append("/".join([prefix, name]))
    return datafiles_list

def load_labels(labels_file):
    labels = dict()
    with open(labels_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            labels[row[0]] = row[1]
    return labels

def load_stopwords(stopwords_file):
    stopwords = []
    with open(stopwords_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            stopwords.append(row[0])
    return stopwords

def digitize_label(label):
    if label == 'spam':
        return 1
    elif label == 'ham':
        return 0
    return None

def evaluate_predictions(ground_path, preds_path):
    """Evaluate predictions against a ground truth file."""
    #We use the labels file as the ground truth file
    actuals = dict()
    with open(ground_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            id, label = row[0], digitize_label(row[1])
            actuals[id] = label

    y_true = []
    y_pred = []
    # Load predictions from file into a dictionary and evaluate predictions against ground truth
    predictions = dict()
    with open(preds_path, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)  # skip header line
        for row in reader:
            id, label = row[0], digitize_label(row[1])
            predictions[id] = label
            if id not in actuals:
                raise KeyError("Missing True Label for document {}".format(id))
            y_true.append(actuals[id])
            y_pred.append(label)

    
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
    print("Accuracy:            {:05.3f}".format((tp + tn) / (tp + tn + fp + fn)))
    print("Precision:           {:05.3f}".format(tp / (tp + fp)))
    print("FPR:                 {:05.3f}".format(fp / (fp + tn)))


model = EmailClassifier()
model.train('C:/Users/akdh/Downloads/data',load_datafile_list('C:/Users/akdh/Downloads/data/train'))
model.load_model('C:/Users/akdh/Downloads/data/train/Train_Model.txt')
model.predict_set('C:/Users/akdh/Downloads/data', load_datafile_list('C:/Users/akdh/Downloads/data/test'), 'C:/Users/akdh/Downloads/data/results.csv')
#evaluate_predictions('C:/Users/USER/Desktop/Academia/Autumn/TextMining/a1-data/train/labels.csv', 'C:/Users/USER/Desktop/Academia/Autumn/TextMining/a1-data/validation/results.csv')
