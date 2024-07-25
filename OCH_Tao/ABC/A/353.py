N = int(input())
H = list(map(int,input().split()))
for i in range(N):
  if H[i]>H[0]:
    print(i+1)
    break
else:
  print(-1)