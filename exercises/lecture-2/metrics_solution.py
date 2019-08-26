"""Computation of classification evaluation measures."""

def confusion_matrix(actual, predicted):
	tp, fn, fp, tn = 0, 0, 0, 0
	
	for a, p in zip(actual, predicted):
		if a == 1:
			if p == 1:
				tp += 1
			else:
				fn += 1
		else:
			if p == 1:
				fp += 1
			else:
				tn += 1						
	
	return tp, fn, fp, tn

def accuracy(actual, predicted):
	tp, fn, fp, tn = confusion_matrix(actual, predicted)
	return (tp + tn) / (tp + fn + fp + tn) 
	
def precision(actual, predicted):
	tp, fn, fp, tn = confusion_matrix(actual, predicted)
	return tp / (tp + fp)

def recall(actual, predicted):
	tp, fn, fp, tn = confusion_matrix(actual, predicted)
	return tp / (tp + fn)

def f1(actual, predicted):
	tp, fn, fp, tn = confusion_matrix(actual, predicted)
	p = precision(actual, predicted)
	r = recall(actual, predicted)
	return (2 * p * r) / (p + r)
	