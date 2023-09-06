N = int(input())
A = list(map(int, input().split()))
rslt = A[0]

if 0 in A:
  print(0)
  exit()

for i in range(1, N):
  rslt *= A[i]
  if rslt > 10**18:
    print(-1)
    exit()

print(rslt)