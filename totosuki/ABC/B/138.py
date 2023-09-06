N = int(input())
A = list(map(int, input().split()))
rslt = 0

for i in range(N):
  rslt += (1 / A[i])

rslt = 1 / rslt
print(rslt)