import pickle
import sys

def eratosthenes(N):
  is_prime = [1] * (N//2)
  is_prime[0] = False
  sqrt_p = (int(N**0.5) + 1) // 2
  for i in range(1, sqrt_p):
    if not is_prime: continue
    p = 2 * i + 1
    for q in range(p*p//2, len(is_prime), p):
      is_prime[q] = 0
  return is_prime

def main():
  N = int(input())
  with open("./prime.pickle", "rb") as f:
    L = pickle.load(f)
  print(2, *[i*2+1 for i in range(N//2) if L[i]], sep = "\n")

if sys.argv[-1] == "ONLINE_JUDGE":
  prime_list = eratosthenes(1000000)
  with open("./prime.pickle", "wb") as f:
    pickle.dump(prime_list, f)
else:
  main()