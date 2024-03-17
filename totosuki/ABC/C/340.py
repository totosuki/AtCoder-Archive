from math import ceil, log2

N = int(input())
a = ceil(log2(N))
base = 2 ** a
diff = base - N
base2 = base * a

print(base2 - (diff * (a+1)))

