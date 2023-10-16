from collections import Counter
import math

def count_square_numbers(S):
    N = len(S)
    dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]
    dp[0][0][1] = 1
    counter = Counter(S)
    factorial = [1]*(N+1)
    for i in range(1, N+1):
        factorial[i] = factorial[i-1]*i
    perm = [factorial[N]//factorial[v] for v in counter.values()]
    perm.sort(reverse=True)
    M = len(perm)
    for i in range(N):
        for smaller in range(2):
            for j in range(M):
                for k in range(10 if smaller else int(S[i])+1):
                    for smaller2 in range(2):
                        for j2 in range(M):
                            if smaller2 and k < int(S[i]) or smaller:
                                dp[i+1][smaller2][j2+(j==0 and k==0)] += dp[i][smaller][j]
    ans = 0
    for i in range(1, N+1):
        if math.isqrt(i)**2 == i:
            s = str(i).zfill(N)
            if sorted(s) == sorted(S):
                ans += dp[N][1][M]
                ans += dp[N][0][M]
    return ans

# テスト
S = "1234"
print(count_square_numbers(S))


# from itertools import permutations
# from math import sqrt

# # 3162277が最大

# N = int(input())
# S = input()
# se = set()
# cnt = 0
# dupe = set()

# for n in range(3162278):
#   se.add(n*n)

# for perm in permutations(S):
#   n = int(''.join(perm))
#   if n in dupe:
#     continue
#   if n in se:
#     dupe.add(n)
#     cnt += 1

# print(cnt)