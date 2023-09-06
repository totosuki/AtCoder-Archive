N = int(input())
s = N
m = s // 60
h = m // 60
s %= 60
m %= 60
h,m,s = map(lambda x: str(x).zfill(2), [h,m,s])
print(":".join([h,m,s]))