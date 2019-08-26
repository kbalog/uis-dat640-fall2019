import unittest

import metrics

class TestEvalMetrics(unittest.TestCase):

	def test_1(self):
		actual = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
		predicted = [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
		tp, fn, fp, tn = metrics.confusion_matrix(actual, predicted)
		self.assertEqual(tp, 3)
		self.assertEqual(fn, 4)
		self.assertEqual(fp, 1)
		self.assertEqual(tn, 2)
		self.assertEqual(metrics.accuracy(actual, predicted), 0.5)
		self.assertEqual(metrics.precision(actual, predicted), 3/4)
		self.assertEqual(metrics.recall(actual, predicted), 3/7)
		self.assertEqual(metrics.f1(actual, predicted), 6/11)

if __name__ == '__main__':
	unittest.main()