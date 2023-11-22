import sys
import pickle

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
  input = sys.stdin.buffer.readline
  with open("./prime.pickle", "rb") as f:
    li = pickle.load(f)
  Q = int(input())

  for _ in range(Q):
    X = int(input())
    if X == 2:
      print("Yes")
    elif X % 2 == 0:
      print("No")
    else:
      X //= 2
      print("Yes") if li[X] else print("No")

if sys.argv[-1] == "ONLINE_JUDGE":
  prime_list = eratosthenes(300000)
  with open("./prime.pickle", "wb") as f:
    pickle.dump(prime_list, f)
else:
  main()