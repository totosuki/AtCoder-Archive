import math
N = int(input())
X = list(map(int, input().split()))
rslt1 = sum([abs(x) for x in X])
rslt2 = math.sqrt(sum([abs(x)**2 for x in X]))
rslt3 = max([abs(x) for x in X])
print(rslt1)
print(rslt2)
print(rslt3)