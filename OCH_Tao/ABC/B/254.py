N = int(input())
ans = [[1]]
for i in range(N-1):
  L = [1]
  for j in range(i):
    L.append(ans[-1][j]+ans[-1][j+1])
  else:
    L.append(1)
    ans.append(L)
for i in ans:
  print(*i)