A, B = map(int, input().split())
for i in range(A, B+1):
  if 100 % i == 0:
    print("Yes")
    break
else:
  print("No")
