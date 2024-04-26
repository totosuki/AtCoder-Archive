N,A,B = map(int,input().split())
cnt = 0
for i in range(1,N+1):
  x = sum(list(map(int,list(str(i)))))
  if A <= x <= B:
    cnt += i
print(cnt)