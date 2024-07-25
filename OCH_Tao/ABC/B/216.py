N = int(input())
S = set()
for i in range(N):
  S.add(input())
print("Yes" if len(S)!=N else "No")