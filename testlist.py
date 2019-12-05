l = [2,5,-9,0,1,8,3]

def max(l):
    res = l[0]
    for val in l[1:]:
        if val > res:
            res = val
    return res

import testhello
def filter2(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

def map2(fn , l):
    res= []
    for val in l:
        res.append(fn(val))
    return res

def inc(x):
    return x + 1

def list2(l):
    res = []
    for val in l:
        res.append(val)
    return res

import unittest
class ListTest(unittest.TestCase):

    def testMax(self):
        self.assertEqual(8, max(l))

    def testFilterEven(self):
        self.assertEqual([2,0,8],filter2(testhello.isEven, l))
        self.assertEqual([2, 5, 3], filter2(testhello.isPrime, l))
        self.assertEqual([2], filter2(testhello.isEven, filter2(testhello.isPrime, l)))
        self.assertEqual([2, 0, 8], list(filter(testhello.isEven, l)))

    def testMap(self):
        self.assertEqual([1,2,3],map2(inc, [0,1,2]))
        self.assertEqual([1, 2, 3], map2(lambda x : x + 1, [0, 1, 2]))
        self.assertEqual([1, 2, 3], map2(lambda x: inc(x), [0, 1, 2]))
        self.assertEqual([1, 2, 3], list(map(lambda x: inc(x), [0, 1, 2])))

    def testMapList(self):
        self.assertEqual([4, 9, 25],
                         list(map(lambda x : x ** 2,
                              filter(lambda x : testhello.isPrime(x), range(6))))
                         )
        # <=>
        self.assertEqual([4, 9, 25],
                         [x ** 2 for x in range(6) if testhello.isPrime(x)]
                         )

    def testValRef(self):
        i = 1
        j = i
        i += 1
        self.assertNotEqual(i, j)
        i = [1]
        j = i
        i.append(2)
        self.assertEqual(i,j)
        i = list(j)
        j.append(3)
        self.assertNotEqual(i, j)

    def testIs(self):
        i = [1,2,3]
        j = [1,2,3]
        self.assertEqual(i , j)
        self.assertFalse(i is j)
        i = j
        self.assertTrue(i is j)
        self.assertIn(1, i)
        # <=>
        self.assertTrue(1 in i)


