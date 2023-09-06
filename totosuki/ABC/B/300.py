H, W = map(int, input().split())
A = []
B = []
for _ in range(H):
  A.append(list(input()))
for _ in range(H):
  B.append(list(input()))

for i in range(H):
  for j in range(W):
    flag = True
    for k in range(H):
      for l in range(W):
        if A[(i+k) % H][(j+l) % W] != B[k][l]:
          flag = False
    if flag:
      print("Yes")
      exit()
print("No")