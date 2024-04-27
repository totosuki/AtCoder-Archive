N = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(N):
  d[A[i]] = i

ans = []
for n in range(1, N+1):
  a = A[n-1] # 交換する相手の値
  b = d[n] # 自分のインデックス
  if n == a: # 自分の値と交換する値が同じ場合はスキップ
    continue
  A[n-1] = n
  A[b] = a
  d[n] = n-1
  d[a] = b
  ans.append((n, a))

print(len(ans))
for a in ans:
  print(*a)