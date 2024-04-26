N,K = map(int,input().split())
A = list(input().split())
for i in range(K):
  del A[0]
  A.append("0")
print(" ".join(A))