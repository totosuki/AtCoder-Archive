N = int(input())
for i in range(1,8):
  if N<2**i:
    print(2**(i-1))
    break