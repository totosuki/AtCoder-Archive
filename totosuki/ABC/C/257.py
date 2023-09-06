_=(i:=input)()
S=i()
W=list(map(int,i().split()))
d={}
r=0
for s,w in zip(S,W):
  r+=(s:=int(s))
  try:d[w]-=1 if s else-1
  except:d[w]=-1 if s else 1
print(max(r,*[r:=r+d[k]for k in sorted(d.keys())]))