N = int(input())
ans = []
for i in range(N):
  A,P,X = map(int,input().split())
  if X-A>0:
    ans.append(P)
print(min(ans) if len(ans)>0 else -1)