from datetime import datetime
start = datetime.now()
noOfCases = int(input())
a = [ int(x) for x in input().split(" ") ]
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

def getMaxIndex(lenOfArray):
    return binary_search_custom(sumOfFirst,lenOfArray)


# print(sumOfFirst[0:10])

for initIndex in range(0,noOfCases):
    # print("current array",initIndex)
    start = datetime.now()
    nearestIndex = getMaxIndex(len(a))
    # print("nearest index",nearestIndex-1)
    modified = a[:nearestIndex]
    # print("modified",modified)
    sumTotal = sum(modified)
    # print("sum", sumTotal)
    # print('Done in ', datetime.now() - start)
    listOfSums.append(sumTotal)
    a.pop(0)
start = datetime.now()
print(max(listOfSums))
# print('max calculation : ', datetime.now() - start)