N = int(input())
A = list(map(int, input().split()))
l = [False for _ in range(N)]
rslt = []
for i in range(N):
  if l[i] == False:
    l[A[i]-1] = True
for i in range(N):
  if l[i] == False:
    rslt.append(i+1)
print(len(rslt))
print(*rslt)