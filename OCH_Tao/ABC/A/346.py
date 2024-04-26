N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N-1):
  L.append(A[i]*A[i+1])
print(" ".join([str(i) for i in L]))