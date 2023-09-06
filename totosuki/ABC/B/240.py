import sys
input = sys.stdin.buffer.readline

N = int(input())
se = set(map(int, input().split()))

print(len(se))