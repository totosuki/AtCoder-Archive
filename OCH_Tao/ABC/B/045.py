A = list(input())
B = list(input())
C = list(input())
i = "a"
while len(A)>=0 and len(B)>=0 and len(C)>=0:
  if i == "a":
    try:
      i = A.pop(0)
    except IndexError:
      print("A")
      break
  if i == "b":
    try:
      i = B.pop(0)
    except IndexError:
      print("B")
      break
  if i == "c":
    try:
      i = C.pop(0)
    except IndexError:
      print("C")
      break