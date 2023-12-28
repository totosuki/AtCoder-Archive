X,Y = input().split()
L = ["A","B","C","D","E","F"]
if L.index(X) == L.index(Y):
  print("=")
elif L.index(X) < L.index(Y):
  print("<")
else:
  print(">")