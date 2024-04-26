N,X = map(int,input().split())
M = []
for i in range(N):
  M.append(int(input()))
M.sort()
cnt = N
X -= sum(M)
while X>=M[0]:
  X -= M[0]
  cnt += 1
print(cnt)