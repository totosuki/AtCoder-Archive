H = int(input())

syoku = 0
for i in range(200):
  syoku += 2**i
  if syoku > H:
    print(i + 1)
    break