N = int(input())
A = list(map(int,input().split()))
cnt = 1
if 0 in A:
  print(0)
  exit()
for i in A:
  cnt*=i
  if cnt>1e18:
    print(-1)
    break
else:
  print(cnt)