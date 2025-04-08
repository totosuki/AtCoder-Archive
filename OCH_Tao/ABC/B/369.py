N = int(input())
L,R = 0,0
cnt = 0
for i in range(N):
  A,S = input().split()
  A = int(A)
  if S=="L":
    if L!=0:
      cnt+=abs(L-A)
    L = A
  else:
    if R!=0:
      cnt+=abs(R-A)
    R = A
print(cnt)