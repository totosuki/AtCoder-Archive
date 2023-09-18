import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A+B)
C_dict = defaultdict(int)

for i in range(N + M): C_dict[C[i]] = i+1

A_rslt = []
B_rslt = []

for a in A: A_rslt.append(C_dict[a])
for b in B: B_rslt.append(C_dict[b])

print(*A_rslt)
print(*B_rslt)