from bisect import bisect_left

LISTOFPRIMES = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
LOOKUP = {}
numberOfcases = int(input())

def findNearestPrime(x):
    distances = []
    for primenumber in LISTOFPRIMES:
        distances.append(abs(x - primenumber))
    return LISTOFPRIMES[distances.index(min(distances))]

def generateLookUp():
    for i in range(0,128):
        LOOKUP[chr(i)] = chr(findNearestPrime(i))
generateLookUp()
# print(LOOKUP)
listOfCases = []
for currentCase in range(0,numberOfcases):
    lengthOfString = input()
    listOfCases.append(input())

for currentCase in listOfCases:
    for letter in currentCase:
        print(LOOKUP[letter],end="")
    print("")