A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
if (A[0]==B[0] and B[1]==C[1]) or (A[1]==B[1] and B[0]==C[0]) or (B[0]==C[0] and C[1]==A[1]) or (B[1]==C[1] and C[0]==A[0]) or (C[0]==A[0] and A[1]==B[1]) or (C[1]==A[1] and A[0]==B[0]):
  print("Yes")
else:
  if (A[1]-B[1])/(A[0]-B[0])+(B[0]-C[0])/(B[1]-C[1])==0:
    print("Yes")
  elif (B[1]-C[1])/(B[0]-C[0])+(C[0]-A[0])/(C[1]-A[1])==0:
    print("Yes")
  elif (C[1]-A[1])/(C[0]-A[0])+(A[0]-B[0])/(A[1]-B[1])==0:
    print("Yes")
  else:
    print("No")