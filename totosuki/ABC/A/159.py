N, M = map(int, input().split())
rslt = 0
for i in range(N):
  rslt += i
for i in range(M):
  rslt += i
print(rslt)