import sys
input = sys.stdin.buffer.readline

N = int(input())
name = {input() for _ in range(N)}

print("Yes") if N != len(name) else print("No")