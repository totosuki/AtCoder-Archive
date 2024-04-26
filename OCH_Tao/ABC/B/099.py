A,B = map(int,input().split())
cnt = 0
for i in range(B-A):
  cnt+=i
print(cnt-A)