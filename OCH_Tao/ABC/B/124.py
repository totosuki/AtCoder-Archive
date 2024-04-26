N = int(input())
H = list(map(int,input().split()))
cnt = 1
for i in range(1,N):
  if all(x<=H[i] for x in H[:i]):
    cnt+=1
print(cnt)