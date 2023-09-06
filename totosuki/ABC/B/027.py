N = int(input())
a = list(map(int, input().split()))
mean = sum(a) / N

#平均値が整数では無い場合exit()
if mean != sum(a) // N:
  print(-1)
  exit()

mean = int(mean)
cnt = 0
i = 0

while i < N:
  if a[i] == mean:
    i += 1
    continue
  
  for j in range(i+1, N):
    check_mean = sum(a[i:j+1]) / (j+1-i)
    if check_mean == mean:
      cnt += j-i
      i = j+1
  
  i += 1

print(cnt)