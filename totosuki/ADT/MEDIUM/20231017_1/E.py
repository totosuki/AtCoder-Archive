from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
C_dict = defaultdict(int)

# dict[要素] = index
for i in range(N+M):
  C_dict[C[i]] = i+1

A_rslt = []
B_rslt = []

for i in range(N):
  A_rslt.append(C_dict[A[i]])
for i in range(M):
  B_rslt.append(C_dict[B[i]])

print(*A_rslt)
print(*B_rslt)