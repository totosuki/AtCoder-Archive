import math
P = int(input())
yens = [math.factorial(i) for i in range(1, 11)]
cnt = 0

for yen in reversed(yens):
  cnt += P // yen
  P -= yen * (P // yen)

print(cnt)