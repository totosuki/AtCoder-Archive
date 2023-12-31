N,K = map(int,input().split())
l = [0]*K
for i in range(N):
  l[i%K] += 1
print(max(l)-min(l))