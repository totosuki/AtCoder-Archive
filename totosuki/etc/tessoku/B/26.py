import pickle
import sys

def check(mid, A, X):
  return A[mid] > X
def binary_search(A, X):
  left = -1
  right = len(A)
  while right - left > 1:
    mid = (left + right) // 2
    if check(mid, A, X):
      right = mid
    else:
      left = mid
  return left

def eratosthenes(N):
  is_prime = [1] * (N+1)
  for p in range(2, int(N**0.5)+1):
    if not is_prime: continue
    for q in range(p*p, N+1, p):
      is_prime[q] = 0
  return is_prime

def main():
  N = int(input())
  with open("./rslt.pickle", "rb") as f:
    L = pickle.load(f)
  id = binary_search(L, N)
  print(*L[:id+1], sep = "\n")

if sys.argv[-1] == "ONLINE_JUDGE":
  prime_list = eratosthenes(1000000)
  rslt = [n for n in range(2, 10**6) if prime_list[n]]
  with open("./rslt.pickle", "wb") as f:
    pickle.dump(rslt, f)
else:
  main()