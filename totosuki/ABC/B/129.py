N = int(input())
W = list(map(int, input().split()))
answer = 10**8

for T in range(N-1):
  answer = min(answer, abs(sum(W[:T+1]) - sum(W[T+1:])))

print(answer)