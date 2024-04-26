N = int(input())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
for i in L:
  tmp = []
  for j in L:
    tmp.append((i[0]-j[0])**2+(i[1]-j[1])**2)
  print(tmp.index(max(tmp))+1)