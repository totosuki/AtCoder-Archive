N = int(input())

tile = [["#"] * 3**N for _ in range(3**N)]

for i in range(1, N+1):
  if i == 1:
    for j in range(1, 3**N, 3):
      for k in range(1, 3**N, 3):
        tile[j][k] = "."
  if i == 2:
    for j in range(3, 3**N, 9):
      for k in range(3, 3**N, 9):
        for l in range(3):
          for m in range(3):
            tile[j+l][k+m] = "."
  if i == 3:
    for j in range(9, 3**N, 27):
      for k in range(9, 3**N, 27):
        for l in range(9):
          for m in range(9):
            tile[j+l][k+m] = "."
  if i == 4:
    for j in range(27, 3**N, 81):
      for k in range(27, 3**N, 81):
        for l in range(27):
          for m in range(27):
            tile[j+l][k+m] = "."
  if i == 5:
    for j in range(81, 3**N, 243):
      for k in range(81, 3**N, 243):
        for l in range(81):
          for m in range(81):
            tile[j+l][k+m] = "."
  if i == 6:
    for j in range(243, 3**N, 729):
      for k in range(243, 3**N, 729):
        for l in range(243):
          for m in range(243):
            tile[j+l][k+m] = "."

[print("".join(t)) for t in tile]