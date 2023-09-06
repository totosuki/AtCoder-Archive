import sys, itertools
input = sys.stdin.buffer.readline

N, M = map(int, input().split())

combo = list(itertools.combinations(range(1, M+1), N))

for i in range(len(combo)):
  print(*combo[i])