A = list(map(int, input().split()))
A.sort()
print(A[-1] - A[0])