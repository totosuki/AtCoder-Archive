N, M = map(int, input().split())
A = list(map(int, input().split()))

mx = (0, 0) # (候補者, 得票数)
hyou = [0] * (N + 1)

for i in range(M):
  hyou[A[i]] += 1
  if mx[1] < hyou[A[i]]:
    mx = (A[i], hyou[A[i]])
  elif mx[1] == hyou[A[i]] and mx[0] > A[i]:
    mx = (A[i], hyou[A[i]])
  print(mx[0])