X, N = map(int, input().split())
P = list(map(int, input().split()))
answer = 1 << 60

for n in range(-5, 103):
  if n in P: continue
  if abs(X - n) < abs(X - answer):
    answer = n

print(answer)