N = int(input())
can = [True] * (2*N+1)

while True:
  takahashi = can.index(True)
  can[takahashi] = False
  print(takahashi + 1, flush = True)
  teki = int(input())
  if teki == 0:
    break
  can[teki-1] = False