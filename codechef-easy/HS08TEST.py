from sys import stdin, stdout
inputvalues = stdin.readline()
withdrawal, balance = inputvalues.split()
withdrawal = int(withdrawal)
initbalance = float(balance)
if withdrawal % 5 == 0:
    calculatedbalance = initbalance - withdrawal - 0.5
    if calculatedbalance > 0:
        print("%.2f" % calculatedbalance)
    else:
        print("%.2f" % initbalance)
else:
    print("%.2f" % initbalance)