N = int(input())
X = list(map(int, input().split()))
print(sum(sorted(X)[N:4*N])/(3*N))
