A,B = map(int,input().split())
cnt = 0
for i in range(A,B+1):
  if str(i) == "".join(list(reversed(str(i)))):
    cnt += 1
print(cnt)