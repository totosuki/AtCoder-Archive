l = []
cnt = 0
for i in range(12):
  l.append(input())
for i in l:
  if "r" in i:
    cnt+=1
print(cnt)