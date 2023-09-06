N = int(input())
A = list(map(int, input().split()))
rslt = []
for a in A:
  if a % 2 == 0:
    rslt.append(a)
print(*rslt)