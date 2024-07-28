N, X, Y = map(int, input().split())
A = sorted(map(int, input().split()), reverse = True)
B = sorted(map(int, input().split()), reverse = True)

cnt = 0
sum = 0

for i in range(N):
  cnt += 1
  sum += A[i]
  if sum > X:
    break

ans = cnt
cnt = 0
sum = 0

for i in range(N):
  cnt += 1
  sum += B[i]
  if sum > Y:
    break

ans = min(ans, cnt)
print(ans)