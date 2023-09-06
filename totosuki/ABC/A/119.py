y, m, d = map(int, input().split("/"))
if m > 4:
  print("TBD")
elif m < 4:
  print("Heisei")
else:
  if d > 30:
    print("TBD")
  else:
    print("Heisei")