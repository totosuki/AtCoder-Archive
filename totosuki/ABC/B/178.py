from operator import xor
a, b, c, d = map(int, input().split())
print(max([a*c, a*d, b*c, b*d]))

# if xor(a < 0, c < 0):
#   print(a * d)
# else:
#   print(b * d)