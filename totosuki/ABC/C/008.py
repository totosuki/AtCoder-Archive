import sys
input = sys.stdin.buffer.readline

N = int(input())
C = [int(input()) for _ in range(N)]
rslt = list()

for i in range(N):
  cnt = 0
  for j in range(N):
    if (C[i] % C[j] == 0) and (i != j):
      cnt += 1
  rslt.append((cnt // 2 + 1) / (cnt + 1))

print(sum(rslt))

# ボツ
# N = int(input())
# C = sorted([int(input()) for _ in range(N)])

# cnt_list = list()
# rslt = list()

# for i in range(N):
#   cnt = 0
#   for j in range(N):
#     if (C[i] % C[j] == 0) and (i != j):
#       cnt += 1
#   cnt_list.append(cnt)

# print(cnt_list)

# for x in cnt_list:  
#   rslt.append((x // 2 + 1) / (cnt + 1))

# print(sum(rslt))

# N <= 8までの場合のみAC
# N = int(input())
# C = [int(input()) for _ in range(N)]

# rslt = []

# for perm in itertools.permutations(C):
#   status = [False] * N
#   for i in range(N-1):
#     a = perm[i]
#     for j in range(i+1, N):
#       if perm[j] % a == 0:
#         status[j] = not status[j]
#   rslt.append(status)

# rslt = [r for i in range(math.factorial(N)) for r in rslt[i]]

# print(rslt.count(False) / math.factorial(N))