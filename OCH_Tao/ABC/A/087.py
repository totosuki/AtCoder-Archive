x = int(input())
A = int(input())
B = int(input())
x -= A

while B - x <= 0:
  x -= B

print(x)