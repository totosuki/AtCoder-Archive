import sys
input = sys.stdin.buffer.readline

N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
rslt = list()

for a in range(N+1):
  b = ((N-a)*E - H - (B*a)) // (D + E) +1
  rslt.append(A*a + C*b)

print(min(rslt))
