ab = list(map(int, input().split()))
ab.sort()
if ab[1] - ab[0] == 1:
  print("Yes")
elif ab[0] == 1 and ab[1] == 10:
  print("Yes")
else:
  print("No")