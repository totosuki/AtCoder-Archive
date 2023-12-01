N = int(input())

for num in range(N, 1000):
  a, b, c = map(int,list(str(num)))
  if a * b == c:
    print(num)
    break