N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
X = T if T in set(C) else C[0]
L = []
for i in range(N):
  if C[i] == X:
    L.append([R[i], i+1])
print(sorted(L, key=lambda x: x[0], reverse=True)[0][1])
