N = int(input())
P = list(map(int,input().split()))
cnt = 0
for i in range(1,N-1):
  if P[i-1]<P[i]<P[i+1] or P[i-1]>P[i]>P[i+1]:
    cnt+=1
print(cnt)