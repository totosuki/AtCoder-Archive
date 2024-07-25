A,B,C,D = map(int,input().split())
while True:
  C-=B
  if C<1:
    break
  A-=D
  if A<1:
    break
print("Yes" if C<A else "No")