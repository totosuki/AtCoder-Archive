N = int(input())
K = int(input())
l = [1]
for i in range(N):
  A = list(map(lambda x:x*2,l))
  B = list(map(lambda x:x+K,l))
  l = A+B
print(min(l))