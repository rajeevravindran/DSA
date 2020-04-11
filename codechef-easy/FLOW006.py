nooftestcases = int(input())

ans = 0

for i in range(nooftestcases):
	(A) = input()
	sum = 0
	for number in A:
		sum = sum + int(number)
	print(sum)