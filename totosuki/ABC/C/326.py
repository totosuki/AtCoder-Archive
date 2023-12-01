N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
answer = []

j = 0
for i in range(N):
  if j != N:
    while A[i] + M > A[j]:
      j += 1
      if j == N:
        break
  answer.append(j - i)

print(max(answer))