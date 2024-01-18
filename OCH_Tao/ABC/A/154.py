S,T = input().split()
A,B = map(int,input().split())
U = input()
if U == S:
  print(f'{A-1} {B}')
else:
  print(f'{A} {B-1}')