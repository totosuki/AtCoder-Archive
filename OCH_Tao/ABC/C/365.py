N,M = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=True)
cnt = M//N
if sum(A)<=M:
  print("infinite")
else:
  tmp = M-cnt*N
  if len([i-min(i,cnt) for i in A if i-min(i,cnt)!=0])<tmp:
    print(cnt)
  else:
    print(cnt+min([i-min(i,cnt) for i in A if i-min(i,cnt)!=0]))