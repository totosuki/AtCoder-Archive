import sys
input = sys.stdin.buffer.readline

L, R = map(int, input().split())
S = input().decode().strip()

S_reversed = "".join(reversed(list(S[L-1:R])))
rslt = S[:L-1] + S_reversed + S[R:]

print(rslt)