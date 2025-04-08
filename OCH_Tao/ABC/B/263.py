N = int(input())
P = list(map(int,input().split()))
i = P[-1]
cnt = 1
while True:
  if i==1:
    print(cnt)
    break
  else:
    i = P[i-2]
    cnt += 1