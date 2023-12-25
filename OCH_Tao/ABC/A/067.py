A,B = map(int,input().split())
if A % 3 == 0:
  print("Possible")
elif B % 3 == 0:
  print("Possible")
elif (A+B) % 3 == 0:
  print("Possible")
else:
  print("Impossible")