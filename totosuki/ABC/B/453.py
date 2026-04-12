T, X = map(int, input().split())
A = list(map(int, input().split()))

before = A[0]
print(0, A[0])

for i in range(1, T+1):
    if abs(A[i] - before) >= X:
        print(i, A[i])
        before = A[i]
