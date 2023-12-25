X,Y = map(int,input().split())
A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
C = [2]
if X in A and Y in A:
  print("Yes")
elif X in B and Y in B:
  print("Yes")
elif X in C and Y in C:
  print("Yes")
else:
  print("No")