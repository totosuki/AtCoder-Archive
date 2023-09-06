K, X = map(int, input().split())
rslt = list(range(X-K+1, X+K))
print(*rslt)