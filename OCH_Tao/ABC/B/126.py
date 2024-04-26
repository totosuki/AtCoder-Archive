N = input()
MMYY = (M:=int(N[:2]))<13 and M!=0
YYMM = (M:=int(N[2:]))<13 and M!=0
if MMYY and YYMM:
  print("AMBIGUOUS")
elif MMYY:
  print("MMYY")
elif YYMM:
  print("YYMM")
else:
  print("NA")