# distutils: language = c++
from libcpp.vector cimport vector
from libcpp cimport bool
from libc.stdio cimport printf, scanf

cdef vector[bool] eratosthenes(int N):
  cdef int i, p, q, sqrt_p
  cdef vector[bool] is_prime = vector[bool](N//2, True)
  is_prime[0] = False
  sqrt_p = (int(N**0.5) + 1) // 2
  for i in range(1, sqrt_p):
    p = 2 * i + 1
    for q in range(p*p//2, is_prime.size(), p):
      is_prime[q] = False
  return is_prime

cdef int main():
  cdef int Q, X
  scanf("%d", &Q)
  cdef vector[bool] li = eratosthenes(300000)

  for _ in range(Q):
    scanf("%d", &X)
    if X == 2:
      printf("Yes\n")
    elif X % 2 == 0:
      printf("No\n")
    else:
      X //= 2
      printf("Yes\n") if li[X] == True else printf("No\n")

main()