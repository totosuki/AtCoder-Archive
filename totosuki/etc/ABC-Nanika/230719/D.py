import sys
input = sys.stdin.buffer.readline

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
cum = [0] * (N)
se = set()
cnt = int()
n_i = int()

for i in range(N):
  cum[i] = cum[i-1] + A[i]

for i in range(N):
  for j in range(i+1, N):
    se.add(cum[j]-cum[i])
    if P in se:
      cnt += 1
      n_i = j

se = set()
for i in range(n_i+1, N):
  for j in range(i+1, N):
    se.add(cum[j]-cum[i])
    if Q in se:
      cnt += 1
      n_i = j

se = set()
for i in range(n_i+1, N):
  for j in range(i+1, N):
    se.add(cum[j]-cum[i])
    if R in se:
      cnt += 1

print(cnt)
print("Yes") if cnt == 3 else print("No")