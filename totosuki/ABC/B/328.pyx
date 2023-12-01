N: int = int(input())
D: int = list(map(int, input().split()))
cnt: int = 0

for i in range(1, N+1):
  for d in range(1, D[i-1]+1):
    month = str(i)
    day = str(d)
    if len(set(list(month + day))) == 1:
      cnt += 1

print(cnt)