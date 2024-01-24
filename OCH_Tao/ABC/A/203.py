A,B,C = map(int,input().split())
if A!=B and B!=C and C!=A:
  print(0)
elif A==B:
  print(C)
elif B==C:
  print(A)
else:
  print(B)