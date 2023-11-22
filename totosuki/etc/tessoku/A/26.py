from numpy import ones
import sys

def eratosthenes(N : int):
  is_prime = ones(N//2, dtype = bool)
  is_prime[0] = 0
  sqrt_p = (int(N**0.5) + 1) // 2
  for i in range(1, sqrt_p):
    if not is_prime[i]: continue
    p = 2 * i + 1
    is_prime[p*p//2::p] = 0
  return is_prime

def main():
  input = sys.stdin.buffer.readline
  Q = int(input())
  prime_list = eratosthenes(300000)
  for _ in range(Q):
    X = int(input())
    if X == 2:
      print("Yes")
    elif X % 2 == 0:
      print("No")
    else:
      X //= 2
      print("Yes" if prime_list[X] else "No")

main()