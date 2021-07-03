from functools import reduce
l = [i*7 for i in range(1,21)]
# fun = lambda a: a%5==0
# extract = filter(fun,l)
# print(list(extract))

def max(a, b):
    if a>b:
        return a
    else:
        return b
max1 = reduce(max, l)
print(max1)
print(max1)
