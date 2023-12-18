import math
A = int(input())
B = int(input())
N = int(input())
x = math.lcm(A,B)
while x < N:
  x += math.lcm(A,B)
print(x)