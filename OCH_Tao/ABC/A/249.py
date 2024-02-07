A,B,C,D,E,F,X = map(int,input().split())
sT = X//(A+C)
tT = sT*A
tT += X%(A+C) if X%(A+C)<A else A
sA = X//(D+F)
tA = sA*D
tA += X%(D+F) if X%(D+F)<D else D
if tT*B>tA*E:
  print("Takahashi")
elif tT*B<tA*E:
  print("Aoki")
else:
  print("Draw")