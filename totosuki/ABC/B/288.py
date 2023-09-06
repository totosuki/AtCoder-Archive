N, K = map(int, input().split())
S = [input() for i in range(N)][:K]
S = sorted(S)
[print(s) for s in S]