import sys; from collections import deque
input = sys.stdin.buffer.readline

N = int(input())
v = list(map(int, input().split()))
v.sort()
v = deque(v)

while len(v) > 1:
  a = v.popleft()
  b = v.popleft()
  v.appendleft((a + b) / 2)

print(v[0])