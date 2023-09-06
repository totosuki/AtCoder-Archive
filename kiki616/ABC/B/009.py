N = int(input())
A = set()
for i in range(N):
    a = int(input())
    A.add(a)
A = list(A)
A.sort()
print(A[-2])