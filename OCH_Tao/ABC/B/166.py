N,K = map(int,input().split())
S = set()
for i in range(K):
  D = int(input())
  A = list(map(int,input().split()))
  S |= set(A)
print(N-len(S))