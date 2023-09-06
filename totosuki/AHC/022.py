import sys; from typing import List, DefaultDict; from collections import defaultdict
input = sys.stdin.buffer.readline

# I/O
def get_cell(N: int) -> DefaultDict[int, List[int]]:
  data = defaultdict(list)
  temp = 0
  for id in range(N):
    Y, X = map(int, input().split())
    temp += 1
    data[temp] = [Y, X, id]
  return data

def set_temperature(temperature: List[List[int]]):
  [print(*t) for t in temperature]
  sys.stdout.flush()

def measure(i: int, y: int, x: int) -> int:
  print(i, y, x, flush = True)
  v = int(input())
  if v == -1:
    print(f"something went wrong. i={i} y={y} x={x}", file=sys.stderr)
    sys.exit(1)
  return v

def answer(result: List[int]):
  print("-1 -1 -1")
  [print(r) for r in result]
  sys.stdout.flush()

# Solve
def make_P(L: int, N: int, data: DefaultDict[int, List[int]]) -> List[List[int]]:
  P = [[0] * L for _ in range(L)]
  for i in range(1, N+1):
    y, x, _ = data[i]
    P[y][x] = i
  return P

def predict(N: int, data: DefaultDict[int, List[int]]) -> List[int]:
  rslt = []
  
  for i in range(N):
    value = measure(i, 0, 0)
    estimate_key = 0
    min_diff = 10000
    
    for temp in data.keys():
      diff = abs(value - temp)
      if diff < min_diff:
        estimate_key = temp
        min_diff = diff
    
    rslt.append(estimate_key - 1)
  
  return rslt

def main():
  L, N, S = map(int, input().split())
  data = get_cell(N)
  P = make_P(L, N, data)
  set_temperature(P)
  result = predict(N, data)
  answer(result)

main()