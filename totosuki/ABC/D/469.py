N, M = map(int, input().split())
A = []; B = []

for _ in range(M):
    a, b = map(int, input().split())
    A.append(a); B.append(b)

x1 = A[0]
x2 = B[0]
pair1 = {x for x in range(1, N+1) if x1 != x}
pair2 = {x for x in range(1, N+1) if x2 != x}

for i in range(M):
    a = A[i]
    b = B[i]

    if not (x1 == a or x1 == b):
        pair1 &= {a, b}
    if not (x2 == a or x2 == b):
        pair2 &= {a, b}

print(len(pair1) + len(pair2) - (x1 in pair2))
