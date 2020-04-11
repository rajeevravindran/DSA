nooftestcases = int(input())

ans = 0

def calcFactorial(n):
	if(n == 0):
		return 1
	else:
		return n*calcFactorial(n-1)

for i in range(nooftestcases):
	(A) = int(input())
	print(calcFactorial(A))