# 未AC
from math import ceil,floor
N = int(input())
l = [N]
cnt = 0
while l[-1]!=1:
  for i in l:
    if i != 1:
      cnt+=i
      l.append(floor(i/2))
      l.append(ceil(i/2))
print(cnt)