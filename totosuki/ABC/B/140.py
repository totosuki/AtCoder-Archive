N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
rslt = 0

for i in range(N):
  rslt += B[i]
  if i == 0: continue
  if A[i] - A[i-1] == 1:
    rslt += C[A[i-1] - 1]

print(rslt)