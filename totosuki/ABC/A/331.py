# Code Golf
M,D,y,m,d=map(int,open(0).read().split())
d=1+d%D
if d<2:m+=1
if m>M:y+=1;m=1
print(y,m,d)


# M, D = map(int, input().split())
# y, m, d = map(int, input().split())
# d += 1
# if d > D:
#   d = 1
#   m += 1
# if m > M:
#   m = 1
#   y += 1
# print(y, m, d)