import numpy as np
N, M = map(int, input().split())
cnt = np.array([[1]*N for _ in range(N)])
for i in range(M):
  A = list(map(lambda x: int(x)-1, input().split()))
  cnt[A[0], A[0]] = 0
  cnt[A[0], A[1]] = 0
  for j in range(1, N-1):
    cnt[A[j], A[j-1]] = 0
    cnt[A[j], A[j]] = 0
    cnt[A[j], A[j+1]] = 0
  else:
    cnt[A[-1], A[-2]] = 0
    cnt[A[-1], A[-1]] = 0
print(np.sum(cnt)//2)
