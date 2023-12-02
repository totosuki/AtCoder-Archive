def main():
  N, K = map(int, input().split())
  A = [0] + list(map(int, input().split()))
  cnt = 0
  sm = A[1]
  right = 1
  for i in range(1, N+1):
    if A[i] <= K: cnt += 1
  for left in range(1, N):
    cnt += right - left
    if right == N: break
    while True:
      if (sm + A[right+1]) <= K:
        cnt += 1
        sm += A[right+1]
        right += 1
      if right == N: break
      if (sm + A[right+1]) > K: break
    sm -= A[left]
  print(cnt)

main()