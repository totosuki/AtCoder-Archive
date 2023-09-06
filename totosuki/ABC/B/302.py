H, W  = map(int, input().split())
S = []
for i in range(H):
  S.append(list(input()))

course = [[1,-1],[1, 0],[1,1],[0,-1],[0,1],[-1,-1],[-1,0],[-1,1]]
for y in range(H):
  for x in range(W):
    if S[y][x] == "s":
      for l in course:
        if 0 <= y+l[0]*4 and y+l[0]*4 < H:
          if 0 <= x+l[1]*4 and x+l[1]*4 < W:
            snuke = [S[y+l[0]*i][x+l[1]*i] for i in range(5)]
            if "".join(snuke) == "snuke":
              for i in range(5):
                print(f"{(y+l[0]*i)+1} {(x+l[1]*i) + 1}")

#monad++

# def find_nuke(S, Y, X) -> bool:
#   global count
#   print(count)

#   if count == 4:
#     return True

#   next_list = [[y, x] for x in [X-1, X, X+1] for y in [Y-1, Y, Y+1] if 0 <= x < W or 0 <= y < H]

#   for l in next_list:
#     if S[l[0]][l[1]] in "nuke"[count]:
#       count += 1
#       return find_nuke(S, l[0], l[1])
  
#   return False

# for i in range(H):
#   for j in range(W):
#     if S[i][j] in "s":
#       isSnuke = find_nuke(S, j, i) #引数の順番がxyのためjとiの順番になっている
