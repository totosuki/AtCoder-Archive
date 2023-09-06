import sys, collections
input = sys.stdin.buffer.readline

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sm = [a+b for a, b in zip(A, B)]
rslt = []

data = []
for i in range(N):
  data.append([A[i],B[i],sm[i],i])

# X
if X:
  data.sort(key = lambda x: (x[0], -x[3]), reverse=True)
  for i in range(X):
    d = data.pop(0)
    rslt.append(d[3]+1)

# Y
if Y:
  data.sort(key = lambda x: (x[1], -x[3]), reverse=True)
  for i in range(Y):
    d = data.pop(0)
    rslt.append(d[3]+1)

# sum
if Z:
  data.sort(key = lambda x: (x[2], -x[3]), reverse=True)
  for i in range(Z):
    d = data.pop(0)
    rslt.append(d[3]+1)

rslt.sort()
print(*rslt, sep = "\n")