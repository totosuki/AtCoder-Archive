N = int(input())
A = list(map(int, input().split()))
weekcnt = 1
rslt = []
tmp = 0
for i in range(len(A)):
  if weekcnt == 8:
    rslt.append(tmp)
    weekcnt = 1
    tmp = 0

  tmp += A[i]
  weekcnt += 1

if weekcnt != 1:
  rslt.append(tmp)

print(*rslt)