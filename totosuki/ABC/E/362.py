N = int(input())
A = list(map(int, input().split()))

seqs = []
MOD = 998244353
cnt = 0
# N = 2の場合
for i in range(N):
  for j in range(i+1, N):
    cnt += 1
    seqs.append([i, j])

ans = [N, cnt] if N >= 2 else [N]

for k in range(3, N+1):
  next_seqs = []
  for seq in seqs:
    diff = A[seq[-1]] - A[seq[-2]]
    for i in range(seq[-1] + 1, N):
      if diff == (A[i] - A[seq[-1]]):
        next_seqs.append(seq.copy() + [i])
  ans.append(len(next_seqs) % MOD)
  seqs = next_seqs.copy()

print(*ans)