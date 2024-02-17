N = int(input())
A = list(map(int,input().split()))
cnt = 0
while all([i%2==0 for i in A]):
  A=list(map(lambda x:x//2,A))
  cnt+=1
print(cnt)