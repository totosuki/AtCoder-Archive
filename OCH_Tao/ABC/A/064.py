R,G,B = input().split()
x = int(R+G+B)
if x % 4 == 0:
  print("YES")
else:
  print("NO")