# import sys
# input = sys.stdin.buffer.readline


H,W=map(int,input().split())
C=[input()for _ in range(H)]
a=[0]*min(H+1,W+1)
def f(r,c):
  t,m=0,min(r,H-1-r,c,W-1-c)
  if m:
    for i in range(1,m+1):
      if C[r-i][c-i]=="."or C[r-i][c+i]=="."or C[r+i][c-i]=="."or C[r+i][c+i]==".":break
      t+=1
    return t
  return 0
for j in range(H*W):
  if C[j//W][j%W]=="#":a[(t:=f(j//W,j%W))]+=1
print(*a[1:])

# import sys
# input = sys.stdin.buffer.readline

# H, W = map(int, input().split())
# C = [list(input().decode().strip()) for _ in range(H)]
# rslt = [0] * min(H, W)

# def fun(row, col):
#   cnt = 0
#   max_cnt = min(min(row, H-1-row), min(col, W-1-col))
#   if max_cnt:
#     for i in range(1, max_cnt + 1):
#       if C[row-i][col-i] == ".": break
#       if C[row-i][col+i] == ".": break
#       if C[row+i][col-i] == ".": break
#       if C[row+i][col+i] == ".": break
#       cnt += 1
#     return cnt
#   else:
#     return 0

# for row in range(H):
#   for col in range(W):
#     if C[row][col] == "#":
#       cnt = fun(row, col)
#       if cnt:
#         rslt[cnt-1] += 1

# print(*rslt)

# sample はAC
# H, W = map(int, input().split())
# C = [list(input().decode().strip()) for _ in range(H)]
# angle = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
# c_p = list()
# rslt = [0] * min(H, W)

# # find cross position
# for row in range(H):
#   for col in range(W):
#     cnt = 0
#     for ag in angle:
#       y = row + ag[0]
#       x = col + ag[1]
#       if not (0 <= y < H) or not (0 <= x < W): continue
#       if C[y][x] == "#":
#         cnt += 1
#     if cnt == 4:
#       c_p.append([row, col])

# # get cross count
# while len(c_p):
#   pos = c_p.pop()
#   cnt_l = list()

#   for ag in angle:
#     y, x = pos
#     cnt = 0
#     y += ag[0]
#     x += ag[1]

#     while C[y][x] == "#":
#       cnt += 1
#       y += ag[0]
#       x += ag[1]
#       if not (0 <= y < H) or not (0 <= x < W):
#         break
    
#     cnt_l.append(cnt)
  
#   min_cnt = min(cnt_l)
#   rslt[min_cnt -1] += 1

# print(*rslt)