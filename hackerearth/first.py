'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

noOfCases = int(input())
a = [ int(x) for x in input().split(" ") ]
b = [ int(x) for x in input().split(" ") ]

originalA = a.copy()

times = 0

for j in range(0,noOfCases):
    minimum = originalA[j]
    print(j)
    # print(sorted(a))
    # print(sorted(b))
    a = originalA.copy()
    for i in range(0, noOfCases):
        if a[i] > b[i] and b[i] > 0:
            while a[i] > minimum:
                times = times + 1
                a[i] = a[i] - b[i]
    if len(set(a)) <= 1:
        print(int(times))
        break
