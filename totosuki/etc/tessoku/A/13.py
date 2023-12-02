N, K = map(int, input().split())
A = [0] + list(map(int, input().split())) + [0]

cnt = 0
right = 1

for left in range(1, N):
  while A[right+1] - A[left] <= K and right < N:
    right += 1
    if right == N: break
  cnt += right - left

print(cnt)