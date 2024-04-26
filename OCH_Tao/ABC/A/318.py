N,M,P = map(int,input().split())
tmp = N-M
cnt = 0
while tmp>=0:
  cnt+=1
  tmp-=P
print(cnt)