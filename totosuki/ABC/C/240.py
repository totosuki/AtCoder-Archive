import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().split())
se = set()
se.add(0)

for _ in range(N):
  a, b = map(int, input().split())
  n_se = set()

  for x in se:
    plus_a = x + a
    plus_b = x + b
    if plus_a <= X:
      n_se.add(plus_a)
    if plus_b <= X:
      n_se.add(plus_b)
  
  se = n_se

print("Yes") if X in se else print("No")