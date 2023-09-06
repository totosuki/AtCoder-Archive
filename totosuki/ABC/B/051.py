K, S = map(int, input().split())
cnt = 0

for X in range(K+1):
  for Y in range(K+1):
    if 0 <= S - (X+Y) <= K:
      cnt += 1

# for X in range(K+1):
#   for Y in range(K+1):
#     for Z in range(K+1):
#       if X + Y + Z == S:
#         cnt += 1

print(cnt)