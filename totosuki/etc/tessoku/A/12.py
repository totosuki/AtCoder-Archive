def check(mid, A):
  ans = 0
  for a in A: ans += mid // a
  return ans

def binary_search(N, X, A):
  left = -1
  right = 10**9 + 5
  while right - left > 1:
    mid = (right + left) // 2
    if check(mid, A) >= X:
      right = mid
    else:
      left = mid
  return right

def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  rslt = binary_search(N, K, A)
  print(rslt)

main()