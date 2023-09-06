H, W, Y, X = map(int, input().split())
S = [input() for _ in range(H)]
cnt = 0

for i in reversed(range(0,X)):
  if S[Y-1][i] == ".":
    cnt += 1
  else:
    break

for i in range(X-1, W):
  if S[Y-1][i] == ".":
    cnt += 1
  else:
    break

for i in reversed(range(0, Y)):
  if S[i][X-1] == ".":
    cnt += 1
  else:
    break

for i in range(Y-1, H):
  if S[i][X-1] == ".":
    cnt += 1
  else:
    break

print(cnt - 3)