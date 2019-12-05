import unittest

def add(x, y=0, z = 0):
    return x + y + z

def isEven(x):
    return x % 2 == 0

isEvenLambda = lambda x : x % 2 == 0

import math
def isPrime(x):
    res = True
    if x < 2:
        res = False
    else:
        for div in range(2,int(math.sqrt(x) + 1)):
            if x % div == 0:
                res = False
                break
    return res


class MyTests(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(2,1+1)

    def testAdd(self):
        i = add(z=1,x=1)
        print(type(add))

    def testIsEven(self):
        self.assertTrue(isEven(8))


    def testIsPrime(self):
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(8))
        f = isPrime
        self.assertTrue(f(7))