N = int(input())
K = int(input())
X = int(input())
Y = int(input())
rslt = 0
if N - K > 0:
  rslt = X * K
  rslt += Y * (N - K)
else:
  rslt = X * N
print(rslt)