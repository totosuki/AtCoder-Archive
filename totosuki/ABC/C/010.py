import sys, math
input = sys.stdin.buffer.readline

txa, tya, txb, tyb, T, V = map(int, input().split())
N = int(input())
answer = "NO"

for i in range(N):
  x, y = map(int, input().split())
  dist_1 = math.sqrt((x-txa)**2 + (y-tya)**2)
  dist_2 = math.sqrt((txb-x)**2 + (tyb-y)**2)
  dist = dist_1 + dist_2
  
  if dist <= (T*V):
    answer = "YES"

print(answer)