N = int(input())
A = list(map(int,input().split()))
print(N*(N+1)*2-sum(A))