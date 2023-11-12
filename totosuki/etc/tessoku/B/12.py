def check(X, N):
  return X**3 + X >= N

def binary_search(N):
  left = 0
  right = N
  while right - left > 0.001:
    mid = (left + right) / 2
    if check(mid, N):
      right = mid
    else:
      left = mid
  return right

def main():
  N = int(input())
  print(binary_search(N))

main()