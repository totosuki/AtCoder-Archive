N, M = map(int, input().split())
A = list(map(int, input().split()))
rslt = N - sum(A)
print(-1) if rslt < 0 else print(rslt)