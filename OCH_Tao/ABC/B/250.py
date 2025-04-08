N,A,B = map(int,input().split())
for i in range(N*A):
  for j in range(N):
    if i//A%2==0:
      if j%2==0:
        print("."*B,end="")
      else:
        print("#"*B,end="")
    else:
      if j%2==0:
        print("#"*B,end="")
      else:
        print("."*B,end="")
  else:
    print()