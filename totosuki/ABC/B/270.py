X, Y, Z = map(int, input().split())

if abs(X) < abs(Y):
  print(abs(X))
else:
  if (X > 0 and Y < 0) or (X < 0 and Y > 0):
    print(abs(X))
  else:
    if abs(Z) < abs(Y):
      if Y > 0 and Z > 0:
        print(abs(X))
      elif Y < 0 and Z < 0:
        print(abs(X))
      else:
        print(abs(X) + abs(Z)*2)
    elif abs(Z) > abs(Y):
      if Y > 0 and Z > 0:
        print(-1)
      elif Y < 0 and Z < 0:
        print(-1)
      else:
        print(abs(X) + abs(Z)*2)
    else:
      print(abs(X) + abs(Z)*2)

# flag = False
# ways = []
# if X > 0:
#   ways = list(range( X))
# elif X < 0:
#   ways = list(range(X, -1))
# count = 0

# #Xに一気に行けるか
# for i in ways:
#   if i == Y and not flag:
#     if X > 0 and Z < Y:
#       count += abs(Z*2)
#     elif X < 0 and Z > Y:
#       count += abs(Z*2)
#     else:
#       print(-1)
#       exit()
#   if i == Z:
#     flag = True
#   count += 1

# print(count)