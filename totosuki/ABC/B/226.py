import sys
input = sys.stdin.buffer.readline

N = int(input())
se = {input().decode().strip() for _ in range(N)}
print(len(se))