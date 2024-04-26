N = int(input())
A = list(map(int,input().split()))
if all([i==A[0] for i in A]):
  print("Yes")
else:
  print("No")