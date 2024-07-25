N,M = map(int,input().split())
H = list(map(int,input().split()))
cnt = 0
for i in H:
  if M>=i:
    cnt+=1
    M-=i
  else:
    break
print(cnt)