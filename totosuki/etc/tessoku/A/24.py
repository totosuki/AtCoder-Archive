from bisect import bisect_left

def dynamic_programming(N, A):
  LEN = 0
  L = []
  dp = [0] * (N)
  for i in range(N):
    pos = bisect_left(L, A[i])
    dp[i] = pos
    if dp[i] >= LEN:
      L.append(A[i])
      LEN += 1
    else:
      L[dp[i]] = A[i]
  return LEN

def main():
  N = int(input())
  A = list(map(int, input().split()))
  rslt = dynamic_programming(N, A)
  print(rslt)

main()