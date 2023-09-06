N = int(input())
K = int(input())
x = 1

for i in range(N):
  if x*2 < x+K:
    x *= 2
  else:
    x += K

print(x)