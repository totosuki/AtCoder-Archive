X = int(input())
money = 100
cnt = 0

while not money >= X:
  money += (money // 100)
  cnt += 1

print(cnt)