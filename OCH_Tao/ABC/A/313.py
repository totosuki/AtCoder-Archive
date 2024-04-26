N = int(input())
P = list(map(int,input().split()))
if N==1:
  print(0)
else:
  if P[0]>max(P[1:]):
    print(0)
  else:
    print(max(P[1:])-P[0]+1)