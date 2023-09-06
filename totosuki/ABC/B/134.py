import math
N, D = map(int, input().split())
dist = D*2 + 1
print(math.ceil(N / dist))