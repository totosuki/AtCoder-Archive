N = int(input())
A = sorted(list(map(int,input().split())))
for i in range(N):
  if A[i]!=i+1:
    print("No")
    break
else:
  print("Yes")