import sys
input = sys.stdin.buffer.readline

N=int(input())
a=[int(input())for _ in[0]*3]
R="NO"
if N in a:R="NO"
else:
  for _ in [0]*100:
    s=N if N<4 else 3
    while N-s in a:s-=1
    if s==0:R="NO"
    N-=s
    if N <= 0:R="YES"
print(R)