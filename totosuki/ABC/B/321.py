N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
answer = -1

score = sum(A[1:N])

for i in range(0, 101):
  tmp = A + [i]
  tmp.sort()
  tmp_score = sum(tmp[1:N-1])
  if tmp_score >= X:
    answer = i
    break

print(answer)