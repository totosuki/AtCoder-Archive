N, M = map(int, input().split())

if (N % 2 == 0):
    if N / M >= 2:
        print("Yes")
    else:
        print("No")
else:
    if (N+1) / M >= 2:
        print("Yes")
    else:
        print("No")