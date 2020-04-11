# from sys import stdin, stdout
# inputvalues = stdin.readlines()
# noOfLines,checkDivisibilty = inputvalues[0].split()
# numbers = inputvalues.pop(0)
# count = 0
# print(noOfLines)
# print(checkDivisibilty)
# print(inputvalues)
# for number in numbers:
#     if int(number) % int(checkDivisibilty) == 0:
#         count = count + 1
# print(count)

(n, k) = map(int, input().split(' '))

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)