N = int(input())
num = 1
while True:
  if num <= N:
    num *= 2
  else:
    print(int(num / 2))
    break