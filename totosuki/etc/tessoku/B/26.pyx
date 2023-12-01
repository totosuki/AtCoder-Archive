from libc.stdio cimport printf, scanf
from libc.stdint cimport int32_t
from libcpp cimport bool
from libcpp.vector cimport vector

def main():
  cdef int32_t N, sqrt_p, i, p, q
  scanf("%d", &N)
  printf("2\n")
  cdef vector[bool] is_prime
  is_prime.reserve(N//2)
  is_prime.assign(N//2, True)
  is_prime[0] = False
  sqrt_p = int(N**0.5 + 1)//2
  for i from 1 <= i < sqrt_p:
    if is_prime[i]:
      p = 2*i+1
      for q from p*p//2 <= q < is_prime.size() by p:
        is_prime[q] = False
  for i from 1 <= i < is_prime.size():
    if is_prime[i]:
      printf("%d\n", 2*i+1)

main()