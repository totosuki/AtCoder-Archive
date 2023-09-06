N = int(input())
A = map(int, input().split())
A = sorted(A)
print(abs(A[0] - A[len(A)-1]))