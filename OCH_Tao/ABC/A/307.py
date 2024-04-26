N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
  L.append(sum(A[7*i:7*(i+1)]))
print(*L)