N = int(input())
A = []
for i in range(N):
  A.append(int(input()))
tmp = 1
cnt = 0
for i in range(N):
  cnt += 1
  tmp = A[tmp-1]
  if tmp == 2:
    print(cnt)
    break
else:
  print(-1)