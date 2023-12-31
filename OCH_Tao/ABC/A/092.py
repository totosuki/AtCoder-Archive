A = int(input())
B = int(input())
C = int(input())
D = int(input())

x = 0
if A < B:
  x += A
else:
  x += B

if C < D:
  x += C
else:
  x += D

print(x)