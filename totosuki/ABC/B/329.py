N = int(input())
A = list(set(list(map(int, input().split()))))

A.sort(reverse = 1)

print(A[1])