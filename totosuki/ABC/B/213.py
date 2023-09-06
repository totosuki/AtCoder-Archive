import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))

A_sorted = sorted(A)
rslt = A.index(A_sorted[-2]) + 1

print(rslt)