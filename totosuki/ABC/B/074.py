N = int(input())
K = int(input())
x = list(map(int, input().split()))

rslt = 0
for i in range(N):
  if abs(K - x[i]) > x[i]:
    rslt += x[i] * 2
  else:
    rslt += abs(K - x[i]) * 2

print(rslt)