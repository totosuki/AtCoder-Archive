A = list(map(int, input().split()))
A.sort()
diff = A[1] - A[0]
for i in range(len(A)-1):
  if diff != A[i+1] - A[i]:
    print("No")
    exit()
print("Yes")