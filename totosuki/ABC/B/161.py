N, M = map(int, input().split())
A = list(map(int, input().split()))
vote_sum = sum(A)
cnt = 0

for i in range(N):
  if A[i] >= vote_sum * (1 / (4*M)):
    cnt += 1

if cnt >= M:
  print("Yes")
else:
  print("No")