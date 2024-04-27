A = list(map(int, input().split()))
B = list(map(int, input().split()))
A2 = sum(A)
B2 = sum(B)

if B2 > A2:
  print(0)
else:
  print(A2 - B2 + 1)