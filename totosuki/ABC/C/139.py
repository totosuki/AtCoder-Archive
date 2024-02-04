N = int(input())
H = list(map(int, input().split()))

answer = 0
cnt = -1
before = 1 << 60
for i in range(N):
  if H[i] <= before:
    cnt += 1
  else:
    answer = max(answer, cnt)
    cnt = 0
  before = H[i]
else:
  answer = max(answer, cnt)

print(answer)
