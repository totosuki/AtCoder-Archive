N,K = map(int,input().split())
A = set(map(int,input().split()))
S = sum(range(1,K+1))
for i in A:
  if i<=K:
    S-=i
print(S)
# MacBookをメモリ不足で落とした極悪コード(戒め)
# N,K = map(int,input().split())
# A = set(list(map(int,input().split())))
# S = set(list(range(1,K+1)))
# print(sum(list(S-A)))