A,B,C,X = map(int,input().split())
if X<=A:
  print(1)
elif B<X:
  print(0)
else:
  print(C/(B-A))