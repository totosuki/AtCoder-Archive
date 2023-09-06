import sys, math
input = sys.stdin.buffer.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

a, b = xb-xa, yb-ya
c, d = xc-xa, yc-ya

rslt = abs(a*d - b*c) / 2

print(rslt)