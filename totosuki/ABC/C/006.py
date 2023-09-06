import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())

for i in range(N+1):
  for j in [0,1]:
    k = N - (i + j)
    if (i*2 + j*3 + k*4) == M and k >= 0:
      print(i, j, k)
      break
  else:
    continue
  break
else:
  print(-1, -1, -1)

# for i in range(N+1):
#   for j in range(N+1-i):
#     k = N - (i + j)
#     if (i*2 + j*3 + k*4) == M:
#       print(i, j, k)
#       break
#   else:
#     continue
#   break
# else:
#   print(-1, -1, -1)