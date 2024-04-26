N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
cnt = 0
for i in range(N):
  if i%2==0:
    cnt+=A[i]
  else:
    cnt-=A[i]
print(cnt)