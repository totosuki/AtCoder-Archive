N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

cnt = 0
right = 1
total = 0

for left in range(1, N+1):
  while right < N+1 and total + A[right] <= K:
    total += A[right]
    right += 1
  total -= A[left]
  cnt += right - left

print(cnt)