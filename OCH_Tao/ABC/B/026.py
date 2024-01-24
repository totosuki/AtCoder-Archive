import math
N = int(input())
l = []
for i in range(N):
  l.append(int(input()))
l.sort(reverse=True)
x = 0
for i in range(N):
  if i%2==0:
    x += l[i]**2
  else:
    x -= l[i]**2
print(x * math.pi)