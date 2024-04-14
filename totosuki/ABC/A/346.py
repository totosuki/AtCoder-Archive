N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N-1):
  B.append(A[i+1] * A[i])

print(*B)