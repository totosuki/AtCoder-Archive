N = int(input())
A = list(map(int, input().split()))
d = {1:0}

for i in range(1, N+1):
    n1 = 2*i
    n2 = 2*i+1
    d[n1] = d[A[i-1]] + 1
    d[n2] = d[A[i-1]] + 1

ans = [d[i] for i in range(1, 2*N+2)]
print(*ans, sep = "\n")