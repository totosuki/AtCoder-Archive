N, X = map(int, input().split())
S = list(map(int, input().split()))
answer = 0

for s in S:
  if s <= X:
    answer += s

print(answer)