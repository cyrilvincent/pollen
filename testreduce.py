import unittest
import functools
class ReduceTest(unittest.TestCase):

    def testSumReduce(self):
        res = functools.reduce(lambda acc, cur : acc + cur, range(10))
        self.assertEqual(45, res)
        res = functools.reduce(lambda acc, cur: acc * cur, range(1, 10), 1)
        self.assertEqual(362880, res)