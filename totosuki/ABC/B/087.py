A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0
x_50 = X /  50
for a in range(A+1):
  for b in range(B+1):
    for c in range(C+1):
      if a*10 + b*2 + c == x_50:
        count += 1

print(count)