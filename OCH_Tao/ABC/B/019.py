S = list(input())
x = S[0]
cnt = 0
l = []
for i in S:
  if i != x:
    l.append(x+str(cnt))
    x = i
    cnt = 1
  else:
    cnt += 1
else:
  l.append(x+str(cnt))
print("".join(l))