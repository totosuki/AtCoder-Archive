import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
S = "".join(sorted(list(S)))

print(S)