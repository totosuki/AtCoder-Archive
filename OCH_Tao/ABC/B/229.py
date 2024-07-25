A,B = map(lambda x:x[::-1],input().split())
for i in range(min(len(A),len(B))):
  if int(A[i])+int(B[i])>9:
    print("Hard")
    break
else:
  print("Easy")