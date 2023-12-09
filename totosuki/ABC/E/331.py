from collections import defaultdict

N, M, L = map(int, input().split())
A = list(map(int, input().split()))
B_base = list(map(int, input().split())) # B に uniqueな値をつける
B = [(B_base[i], i+1) for i in range(M)]

B.sort(reverse = True)

bad = defaultdict(set) # 選べない組み合わせ
for _ in range(L):
  c, d = map(int, input().split())
  bad[c-1].add(d)

rslt = 0

for i in range(N):
  for b in B:
    b_val, b_idx = b
    if b_idx not in bad[i]:
      rslt = max(rslt, A[i] + b_val)
      break

print(rslt)