import sys
input = sys.stdin.buffer.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N-1)]
se = {data[0][0], data[0][1]}

for d in data:
  se = se & {d[0], d[1]}

print("Yes") if se else print("No")