from datetime import datetime
start = datetime.now()
noOfCases = int(input())
a = [ int(x) for x in input().split(" ") ]
print('Parsing Time: ', datetime.now() - start)
listOfSums = []

for initIndex in range(0,noOfCases):
    print("current index: ",initIndex,end="")
    start = datetime.now()
    sumTotal = 0
    for counter in range(0,noOfCases):
        sliceEnd = initIndex + counter + 1
        # print(initIndex,":",sliceEnd)
        if sliceEnd > noOfCases:
            break
        t = a[initIndex:sliceEnd]
        # print(t)
        sumTotal += sum(t)
        initIndex = sliceEnd
    print('Done in ', datetime.now() - start)
    listOfSums.append(sumTotal)
start = datetime.now()
print(max(listOfSums))
print('max calculation : ', datetime.now() - start)