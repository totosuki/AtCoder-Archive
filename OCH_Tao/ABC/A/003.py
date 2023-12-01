n = int(input())
money = 0

for i in range(n):
  i += 1
  money += i * 10000

x = money // n
print(x)