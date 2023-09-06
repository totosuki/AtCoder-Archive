X = int(input())
se = {1}
for n in range(100):
  for m in range(2, 10):
    x = n ** m
    if x <= X:
      se.add(x)

print(max(se))

#import math
# X = int(input())

# print(int(math.sqrt(X)) ** 2)