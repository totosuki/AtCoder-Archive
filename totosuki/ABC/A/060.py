A, B, C = input().split()
flag = False
if A[-1] != B[0]:
  flag = True
if B[-1] != C[0]:
  flag = True
print("NO") if flag else print("YES")