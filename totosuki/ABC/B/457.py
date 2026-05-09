N = int(input())
L = []
A = []

for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)

X, Y = map(int, input().split())

print(A[X - 1][Y - 1])
