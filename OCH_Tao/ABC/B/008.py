N = int(input())
l = []
x = []
for i in range(N):
  l.append(input())
for i in range(N):
  x.append(l.count(l[i]))
y = x.index(max(x))
print(l[y])