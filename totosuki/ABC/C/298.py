import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N = int(input())
Q = int(input())

box = defaultdict(list)
card = defaultdict(set)

for _ in range(Q):
  num, *args = map(int, input().split())
  
  if num == 1:
    i, j = args
    box[j].append(i)
    card[i].add(j)
  elif num == 2:
    i = args[0]
    print(*sorted(box[i]))
  else:
    i = args[0]
    print(*sorted(list(card[i])))