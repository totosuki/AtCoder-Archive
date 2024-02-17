H,W = map(int,input().split())
S = []
for i in range(H):
  S.append(list(input()))
for i in range(H):
  l = []
  for j in range(W):
    if S[i][j]=="#":
      l.append("#")
    else:
      cnt=0
      if i>0 and j>0:
        if S[i-1][j-1]=="#":
          cnt+=1
      if i>0:
        if S[i-1][j]=="#":
          cnt+=1
      if i>0 and j<W-1:
        if S[i-1][j+1]=="#":
          cnt+=1
      if j>0:
        if S[i][j-1]=="#":
          cnt+=1
      if j<W-1:
        if S[i][j+1]=="#":
          cnt+=1
      if i<H-1 and j>0:
        if S[i+1][j-1]=="#":
          cnt+=1
      if i<H-1:
        if S[i+1][j]=="#":
          cnt+=1
      if i<H-1 and j<W-1:
        if S[i+1][j+1]=="#":
          cnt+=1
      l.append(cnt)
  else:
    print("".join([str(i) for i in l]))