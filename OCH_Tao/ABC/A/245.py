A,B,C,D = map(int,input().split())
if A<C:
  flag = True
elif C<A:
  flag = False
else:
  if B<D:
    flag = True
  elif D<B:
    flag = False
  else:
    flag = True
if flag:
  print("Takahashi")
else:
  print("Aoki")