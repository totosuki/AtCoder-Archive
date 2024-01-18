A = input()
L = list(A)
if A == "a":
  print(-1)
elif len(L)==1:
  x = ord(L[-1])-1
  print(chr(x))
else:
  del L[-1]
  print("".join(L))