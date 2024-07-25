A,B = map(int,input().split())
cnt = 1
ans = 0
while cnt<B:
  ans+=1
  cnt+=A-1
print(ans)