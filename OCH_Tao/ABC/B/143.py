N = int(input())
D = list(map(int,input().split()))
cnt = 0
for i in range(N-1):
  for j in range(i+1,N):
    cnt+=D[i]*D[j]
print(cnt)