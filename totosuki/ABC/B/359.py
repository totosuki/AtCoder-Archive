N = int(input())
A = list(map(int, input().split()))
cnt = 0

before = A[0]

for i in range(2, 2 * N):
  if before == A[i] and A[i-1] != A[i]:
    cnt += 1
  before = A[i-1]

print(cnt)