N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(len(B)):
    if B[i] in A:
        A.remove(B[i])

print(*A)