N = int(input())
W = list(map(int, input().split()))
rslt = []

for i in range(N):
  rslt.append(abs(sum(W[:i+1]) - sum(W[i+1:])))

print(min(rslt))