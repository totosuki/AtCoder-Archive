from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(accumulate([0]+A))
R = [0]*100009
ans = 0

for i in range(1, N+1):
  if i == 1:
    R[i] = 1
  else:
    R[i] = R[i-1]

  while R[i] <= N and B[R[i]]-B[i-1] <= K:
    R[i] += 1

  ans += R[i]-i

print(ans)
