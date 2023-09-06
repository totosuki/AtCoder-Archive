N = input()
if int(N) >= 42:
  N = str(int(N) + 1)
  print("AGC" + N.zfill(3))
else:
  print("AGC" + N.zfill(3))