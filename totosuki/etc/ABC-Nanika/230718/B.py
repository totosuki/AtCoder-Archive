N = int(input())
S = [0] + list(map(int, input().split()))
rslt = []

for i in range(1, N+1):
  rslt.append(S[i] - S[i-1])

print(*rslt)