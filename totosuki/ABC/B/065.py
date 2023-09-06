N = int(input())
a = [int(input()) for _ in range(N)]

pos = 1
cnt = 1
i = 0
while i < N:
  if a[pos-1] == 2:
    print(cnt)
    exit()
  else:
    pos = a[pos-1]
  cnt += 1
  i += 1
print(-1)