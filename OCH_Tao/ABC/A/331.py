M,D = map(int,input().split())
YMD = list(map(int,input().split()))
if YMD[2]<D:
  YMD[2]+=1
  print(*YMD)
else:
  YMD[2]=1
  if YMD[1]<M:
    YMD[1]+=1
    print(*YMD)
  else:
    YMD[1]=1
    YMD[0]+=1
    print(*YMD)
