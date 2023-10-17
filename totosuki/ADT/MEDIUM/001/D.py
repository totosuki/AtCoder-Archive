# 192byte
# N,M=map(int,input().split())
# L=[[0]*N for _ in[0]*N]
# a="Yes"
# for _ in[0]*M:
#  K,*X=map(int,input().split())
#  for x in X:
#   for y in X:L[x-1][y-1]=1
# print("YNeos"[sum(sum(l)for l in L)!=N*N::2])



# N, M = map(int, input().split())
# ok = [[False] * N for _ in range(N)]
# answer = "Yes"

# for _ in range(M):
#   K, *X = map(int, input().split())
#   for x in X:
#     row = x - 1
#     for y in X:
#       col = y - 1
#       ok[row][col] = True

# for row in range(N):
#   for col in range(N):
#     if ok[row][col] == False:
#       answer = "No"

# print(answer)