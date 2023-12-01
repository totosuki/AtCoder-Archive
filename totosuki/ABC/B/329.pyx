# distutils: language=c++
from libcpp.vector cimport vector
from libcpp.algorithm cimport sort as csort
from libc.stdio cimport printf, scanf

def main():
  cdef int i
  cdef vector[int] A
  cdef int elem

  scanf("%d", &i)

  for _ in range(i):
    scanf("%d", &elem)
    A.push_back(elem)

  cdef vector[int] L = list(set(A))

  csort(L.rbegin(), L.rend())
  printf("%d\n", L[1])

main()