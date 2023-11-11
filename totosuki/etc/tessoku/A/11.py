def binary_search(N, X, A):
  left = -1
  right = N
  while right - left > 1:
    mid = (left + right) // 2
    if A[mid] >= X:
      right = mid
    else:
      left = mid
  return right

def main():
  N, X = map(int, input().split())
  A = list(map(int, input().split()))
  rslt = binary_search(N, X, A)
  print(rslt + 1)

main()