from itertools import permutations
N = int(input())
S = [input() for _ in range(N)]
for i, j in permutations(S, 2):
  X = i+j
  if X == X[::-1]:
    print("Yes")
    break
else:
  print("No")
