N = int(input())
cnt = 0
for i in range(N):
  if input()=="For":
    cnt+=1
else:
  if N//2<cnt:
    print("Yes")
  else:
    print("No")