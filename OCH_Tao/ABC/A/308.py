S = list(map(int,input().split()))
flag = True
for i in range(7):
  if S[i]>S[i+1]:
    flag=False
    break
if min(S)<100 or max(S)>675:
  flag=False
if any([i%25!=0 for i in S]):
  flag=False
if flag:
  print("Yes")
else:
  print("No")