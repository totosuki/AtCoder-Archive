import sys
input = sys.stdin.buffer.readline

S = input().decode().rstrip().replace("00","?")

print(len(S))