import math
M = int(input())
km = M/1000
if km < 0.1:
  print("00")
elif 0.1 <= km <= 5:
  if len(str(math.trunc(km*10)))==1:
    print(f"0{math.trunc(km*10)}")
  else:
    print(math.trunc(km*10))
elif 6 <= km <= 30:
  print(50+int(km))
elif 35 <= km <= 70:
  print((int(km)-30)//5+80)
else:
  print("89")