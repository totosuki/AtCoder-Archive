N = int(input())
D, X = map(int, input().split())
rslt = X

for _ in range(N):
  A = int(input())
  rslt += 1 + ((D-1) // A)

print(rslt)