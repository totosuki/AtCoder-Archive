H,W = map(int,input().split())
S = ""
for i in range(H):
  S+=input()
X = S.index("o")
Y = S.rindex("o")
print(abs(X//W-Y//W)+abs(X%W-Y%W))