N = int(input())
a = [0,0,0,1]
for i in range(N):
  a.append((a[1]+a[2]+a[3])%10007)
  del a[0]

print(a[0])