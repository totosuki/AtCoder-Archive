from math import sqrt

B = int(input())

a = 1

while a ** a <= B+1:
  if a ** a == B:
    print(a)
    exit()
  a += 1

print(-1)