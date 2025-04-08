N = int(input())
A = list(map(int,input().split()))
cnt = 0
while True:
  cnt+=1
  A.sort(reverse=True)
  A[0]-=1
  A[1]-=1
  if sorted(A,reverse=True)[1]<1:
    print(cnt)
    break