A,B = input().split()
L = ["2","3","4","5","6","7","8","9","10","11","12","13","1"]
x = L.index(A)
y = L.index(B)
if x == y:
  print("Draw")
elif x > y:
  print("Alice")
else:
  print("Bob")