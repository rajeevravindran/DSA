from bisect import bisect_left

LISTOFPRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                223, 227, 229, 233, 239, 241, 251, 257]

# numberOfcases = int(input())

def findNearestPrime(x):
    print("searching for",x)
    lo = 0
    hi = None
    hi = hi if hi is not None else len(LISTOFPRIMES)
    pos = bisect_left(LISTOFPRIMES, x, lo, hi)
    print("Found ",LISTOFPRIMES[pos])
    distanceFromPrime = LISTOFPRIMES[pos] - x
    if x - distanceFromPrime in LISTOFPRIMES and distanceFromPrime > 0:
        return LISTOFPRIMES[pos - 1]
    return LISTOFPRIMES[pos] if pos != hi and LISTOFPRIMES[pos] >= x else -1

print(chr(findNearestPrime(ord('y'))))
# listOfCases = []
# for currentCase in range(0,numberOfcases):
#     lengthOfString = input()
#     listOfCases.append(input())
#
# for currentCase in listOfCases:
#     print(currentCase)
#     for letter in currentCase:
#         print(chr(findNearestPrime(ord(letter))),end="")
#     print("")

'''
AvfmaLgLRpQadLyThsxV
CqemaIgISqOaeISgqqS
CqemaIgISqOaeIqSgqqSqkSqaG
'''