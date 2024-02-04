N = int(input())
A = list(map(int, input().split()))
now = 0
mn = 0

for i in range(N):
  now += A[i]
  mn = min(mn, now)

rslt = mn * -1

for i in range(N):
  rslt += A[i]

print(rslt)