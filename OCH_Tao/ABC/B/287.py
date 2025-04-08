N,M = map(int,input().split())
S = []
for i in range(N):
  S.append(input())
T = set()
for i in range(M):
  T.add(input())
cnt = 0
for i in S:
  if i[3:] in T:
    cnt+=1
print(cnt)