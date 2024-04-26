N = int(input())
A = list(map(int,input().split()))
cnt = 0.0
for i in A:
  cnt+=1/i
print(1/cnt)