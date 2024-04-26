S = list(input())
cnt = 1
for i in S:
  if i.isupper():
    print(cnt)
    break
  else:
    cnt+=1