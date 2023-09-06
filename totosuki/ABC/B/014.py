n, X = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = bin(X)[2:].zfill(n)

rslt = 0
for i in range(n):
  if int(b[i]):
    rslt += a[i]
print(rslt)