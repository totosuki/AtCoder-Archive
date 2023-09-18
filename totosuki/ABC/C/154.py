import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
A_len = len(A)

print("YES") if len(set(A)) == A_len else print("NO")