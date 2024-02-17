N = int(input())
A = list(map(int, input().split()))

for i in range(N-1):
  S, T = map(int, input().split())
  A[i+1] += (A[i] // S) * T

print(A[N-1])