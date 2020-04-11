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

a_temp = a.copy()

# times = 0
# minimum = 5
# print(minimum)
# print(sorted(a))
# print(sorted(b))
# for i in range(0, noOfCases):
#     if a[i] > b[i] and b[i] > 0:
#         while(a[i] > minimum):
#             times = times + 1
#             a[i] = a[i] - b[i]
# if not len(set(a)) <= 1:
#     print(-1)
# else:
#     print(int(times))
print(a)
print(b)
for j in range(0,noOfCases):
    for i in range(0, noOfCases):
        if a_temp[i] > b[i]:
            a_temp[i] = a_temp[i] - b[i]
print(a_temp)
minimum = max(a_temp)
print(minimum)
times = 0
for i in range(0, noOfCases):
    if a[i] > b[i] and b[i] > 0:
        while(a[i] > minimum):
            times = times + 1
            a[i] = a[i] - b[i]
print(a)
if not len(set(a)) <= 1:
    print(-1)
else:
    print(int(times))
