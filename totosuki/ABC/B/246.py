import sys, math
input = sys.stdin.buffer.readline

A, B = map(int, input().split())

dist = math.sqrt(A**2 + B**2)
rslt_A = A/dist
rslt_B = B/dist

print(rslt_A, rslt_B)