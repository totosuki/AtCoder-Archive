N, M = map(int, input().split())
A = [0] * M
B = [0] * M

for _ in range(N):
    a, b = map(int, input().split())
    A[a-1] += 1
    B[b-1] += 1

for i in range(M):
    print(B[i] - A[i])
