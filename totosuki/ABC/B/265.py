N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonuses = [list(map(int, input().split())) for _ in range(M)]

for bonus in bonuses:
  A[bonus[0]-1] -= bonus[1]

for i in range(N-1):
  T -= A[i]

  if T <= 0:
    print("No")
    exit()

print("Yes")