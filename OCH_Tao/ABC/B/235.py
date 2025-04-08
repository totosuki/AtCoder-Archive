N = int(input())
H = list(map(int,input().split()))
ans = 0
for i in H:
  if i>ans:
    ans=i
  else:
    break
print(ans)