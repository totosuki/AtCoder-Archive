n = int(input())
a = list(map(int, input().split()))
rslt = 0

for i in range(n):
  cnt = 0
  while (a[i] % 3 == 2) or (a[i] % 2 == 0):
    a[i] -= 1
    cnt += 1
  rslt += cnt

print(rslt)