N, X = map(int, input().split())
L = list(map(int, input().split()))
D = [0]

for i in range(N):
  rslt = D[i] + L[i]
  D.append(rslt)

cnt = 0
for i in range(N+1):
  if D[i] <= X:
    cnt += 1

print(cnt)