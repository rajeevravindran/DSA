# from datetime import datetime
# start = datetime.now()
noOfCases = int(input())
a = [ int(x) for x in input().split() ]
# print('Parsing Time: ', datetime.now() - start)
listOfSums = []
from bisect import bisect_left
def binary_search_custom(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    if pos != hi and a[pos] == x:
        return a[pos]
    return a[pos-1] if pos != hi and a[pos] >= x else -1

sumOfFirst = [int((i * (i + 1)) / 2) for i in range(0,noOfCases) if i > 0]
LOOKUP = []

def getMaxIndex(lenOfArray):
    return binary_search_custom(sumOfFirst,lenOfArray)

def generateLookup(array):
    # elem =0
    LOOKUP.append(array[0])
    for i in range(1,len(array)):
        elem = LOOKUP[i - 1] + a[i]
        LOOKUP.append(elem)
    # print(LOOKUP)
    # return elem

def modify(a):
    del a[0]


generateLookup(a)

sumShift = 0
# print(LOOKUP)
for initIndex in range(0,noOfCases):
    # print(initIndex)
    nearestIndex = getMaxIndex(len(a))
    # print("current array",a)
    # start = datetime.now()
    # print("nearest index",nearestIndex)
    calculatedSum = LOOKUP[nearestIndex-1] - sumShift
    listOfSums.append(calculatedSum)
    # print("calculatedSum",calculatedSum)
    sumShift = LOOKUP[0]
    modify(LOOKUP)
    modify(a)
    # a.pop(0)
    # print("sumshift",sumShift)
# start = datetime.now()
# print(listOfSums)
print(max(listOfSums))
# print('max calculation : ', datetime.now() - start)