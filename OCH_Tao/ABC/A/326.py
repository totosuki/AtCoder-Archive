x,y = input().split()
n = int(y) - int(x)

if n > 2:
  steps = False
elif n < -3:
  steps = False
else:
  steps = True

if steps == False:
  print("No")
elif steps == True:
  print("Yes")