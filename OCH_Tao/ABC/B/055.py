N = int(input())
p = 1
for i in range(1,N+1):
  p*=i
  p%=(int(1e9)+7)
print(p)