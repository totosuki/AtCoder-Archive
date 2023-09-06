import sys
import numpy as np
input = sys.stdin.buffer.readline

T = int(input())

for i in range(T):
  answer = "No"
  N, K = map(int, input().split())

  min_K = sum(list(map(int, np.base_repr(N,3))))

  if N % 2 == 0:
    if min_K <= K and K % 2 == 0:
      answer = "Yes"
  elif N % 2 == 1:
    if min_K <= K and K % 2 == 1:
      answer = "Yes"

  print(answer)