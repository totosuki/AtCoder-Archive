H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
S = []
for i in range(H):
  S.append(list(input()))
T = input()
C = 0
for i in T:
  if i == "U" and S[X-1][Y] != "#":
    X -= 1
  elif i == "D" and S[X+1][Y] != "#":
    X += 1
  elif i == "L" and S[X][Y-1] != "#":
    Y -= 1
  elif i == "R" and S[X][Y+1] != "#":
    Y += 1
  if S[X][Y] == "@":
    C += 1
    S[X][Y] = "."
print(X+1, Y+1, C)
