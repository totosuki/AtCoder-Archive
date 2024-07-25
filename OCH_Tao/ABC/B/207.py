A,B,C,D = map(int,input().split())
cnt = [A,0]
ans = 0
for i in range(int(1e6)):
  ans+=1
  cnt[0]+=B
  cnt[1]+=C
  if cnt[0]<=cnt[1]*D:
    print(ans)
    break
else:
  print(-1)