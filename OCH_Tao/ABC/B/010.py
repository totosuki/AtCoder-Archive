N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
  x = A[i]
  while x%2==0 or x%3==2:
    cnt += 1
    x -= 1
print(cnt)