import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
print(*[a for a in A if a != X])