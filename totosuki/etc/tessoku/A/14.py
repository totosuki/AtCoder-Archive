def check(mid, X, A):
  return A[mid] >= X

def binary_search(N, X, A):
  left = -1
  right = N-1
  while right - left > 1:
    mid = (left + right) // 2
    if check(mid, X, A):
      right = mid
    else:
      left = mid
  return A[right]

def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  C = list(map(int, input().split()))
  D = list(map(int, input().split()))
  answer = "No"
  E = []
  F = []
  for a in A:
    for b in B:
      E.append(a + b)
  for c in C:
    for d in D:
      F.append(c + d)
  F.sort()
  for e in E:
    X = binary_search(len(F), K - e, F)
    if K - e == X:
      answer = "Yes"
  print(answer)

main()