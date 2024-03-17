A, B = map(int, input().split())

for i in range(10):
  if A + B != i:
    print(i)
    break