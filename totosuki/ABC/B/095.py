N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
cnt = N
X -= sum(M)
min_i = M.index(min(M))

cnt += X // M[min_i]

print(cnt)