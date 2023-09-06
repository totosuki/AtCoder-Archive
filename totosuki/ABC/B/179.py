N = int(input())
cnt = 0
answer = "No"

for i in range(N):
  d1, d2 = map(int, input().split())
  if d1 == d2:
    cnt += 1
  else:
    cnt = 0
  if cnt == 3:
    answer = "Yes"

print(answer)