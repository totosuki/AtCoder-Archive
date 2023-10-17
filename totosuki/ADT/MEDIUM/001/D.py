N, M = map(int, input().split())
ok = [[False] * N for _ in range(N)]
answer = "Yes"

for _ in range(M):
  K, *X = map(int, input().split())
  for x in X:
    row = x - 1
    for y in X:
      col = y - 1
      ok[row][col] = True

for row in range(N):
  for col in range(N):
    if ok[row][col] == False:
      answer = "No"

print(answer)