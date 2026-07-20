N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

zero = 0
one = 0
Azero = A.copy()
Aone = A.copy()
Azero[0] = 0
Aone[0] = 1

if A[0] != 0: zero += 1
if A[0] != 1: one += 1

for i in range(N-1):
    if (Azero[i]+Azero[i+1]) % 2 != B[i]:
        Azero[i+1] += 1
        zero += 1
    
    if (Aone[i]+Aone[i+1]) % 2 != B[i]:
        Aone[i+1] += 1
        one += 1

print(min(zero, one))
