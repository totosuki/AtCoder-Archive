N = int(input())
A = []
for i in range(N):
  A.append(list(map(int,input().split())))
ans = 1
for i in range(N):
  tmp = [ans-1,i]
  ans = A[max(tmp)][min(tmp)]
print(ans)