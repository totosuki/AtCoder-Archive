from math import ceil
A,B,W = map(int,input().split())
W*=1000
if W//A!=W//B:
  print(ceil(W/B),W//A,sep=" ")
else:
  if W%A>B-A or W%B>B-A:
    print("UNSATISFIABLE")
  else:
    print(W//A,W//B,sep=" ")