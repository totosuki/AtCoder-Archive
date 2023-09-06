D = int(input())
N = int(input())
B = [0] * (D+2)
cum = [0] * (D+1)

for i in range(N):
  l, r = map(int, input().split())
  B[l] += 1
  B[r+1] -= 1

for i in range(1, D+1):
  cum[i] = cum[i-1] + B[i]
  print(cum[i])


# --TLE--
# D = int(input())
# N = int(input())
# st = time.perf_counter()
# cum = [0]*D

# for i in range(N):
#   L, R = map(int, input().split())
#   for j in range(L-1, R):
#     cum[j] += 1

# print(*cum, sep = "\n")