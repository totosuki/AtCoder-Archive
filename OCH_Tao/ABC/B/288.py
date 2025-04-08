N,K = map(int,input().split())
L = []
for i in range(N):
  S = input()
  if i<K:
    L.append(S)
print(*sorted(L),sep="\n")