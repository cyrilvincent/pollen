def filter(fn, l):
    for val in l:
        if fn(val):
            yield val

def map(fn , l):
    for val in l:
        yield fn(val)

def range(nb):
    i = 0
    while i < nb:
        yield i
        i+=1

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

def infiniteYield():
    i = 0
    while True:
        yield i
        i += 1


import testhello
print(filter(testhello.isPrime, range(100)))
res = filter(testhello.isEven, filter(testhello.isPrime, range(1000000000000000000)))
# for val in res:
#     print(val)
#res = filter(testhello.isEven, range(100))
#Lazy loading

#res = map(lambda x : x ** 2, filter(testhello.isPrime, range(1000000000000000000)))
res = filter(testhello.isPrime, range(1000000000000000000))
res = map(lambda x : x ** 2, res)
for val in res:
    print(val)


res = (x ** 2 for x in range(1000000000000000000) if testhello.isPrime(x))

res = [x ** 2 for x in range(1000000000000000000) if testhello.isPrime(x)]
# <=>
res = list((x ** 2 for x in range(1000000000000000000) if testhello.isPrime(x)))

res = infiniteYield()
for i in res:
    print(i)