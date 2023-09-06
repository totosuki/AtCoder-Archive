N,M = map(int, input().split())
tile = [input() for _ in range(N)]
test = ["###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###"]

for i in range(N-8):
  for j in range(M-8):
    flag = True
    for k in range(9):
      for l in range(9):
        if tile[i+k][j+l] == "#" and (test[k][l] == "#" or test[k][l] == "?"):
          continue
        elif tile[i+k][j+l] == "." and (test[k][l] == "." or test[k][l] == "?"):
          continue
        else:
          flag = False
    
    if flag:
      print(i+1, j+1)


