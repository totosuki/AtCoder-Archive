N = int(input())
S = set()
for i in range(N):
  A = tuple(map(int,input().split()))
  S.add(A)
print(len(S))