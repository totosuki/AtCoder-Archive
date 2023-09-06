h_a, w_a = map(int, input().split())
A = [input() for _ in range(h_a)]
h_b, w_b = map(int, input().split())
B = [input() for _ in range(h_b)]
h_x, w_x = map(int, input().split())
X = [input() for _ in range(h_x)]

def return_map(x,y):
  max_x = max([w_b, w_a+x])
  max_y = max([h_b, h_a+y])

  for row in range(max_y):
    for col in range(max_x):
      if row >= h_a

C = []

for y in range(h_a):
  for x in range(w_a):
    tmp = []
    if 
# tmp = [[False] * w_a]*h_a
# for row in range(h_a):
#   for col in range(w_a):
#     if A[row][col] == "#":
#       A[row][col] = True
# A = tmp
# tmp = [[False] * w_b]*h_b
# for row in range(h_b):
#   for col in range(w_b):
#     if B[row][col] == "#":
#       B[row][col] = True
# B = tmp
# tmp = [[False] * w_x]*h_x
# for row in range(h_x):
#   for col in range(w_x):
#     if X[row][col] == "#":
#       X[row][col] = True
#     else:
#       X[row][col] = False
# X = tmp

# print(A)
# print(B)
# print(X)

# for i in range(h_a):
#   for j in range(w_a):
#     for k in range(h_b):
#       for l in range(w_b):
        