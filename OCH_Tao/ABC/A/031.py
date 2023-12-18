A,D = map(int,input().split())
Aup = (A+1)*D
Dup = A * (D+1)
if Aup >= Dup:
  print(Aup)
else:
  print(Dup)