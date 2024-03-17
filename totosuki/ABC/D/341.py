from math import gcd, lcm

N, M, K = map(int, input().split())

lcm_nm = lcm(N, M) # 最小公倍数

# 1からlcm_nmまでの数で割り切れる数を数える
cnt = ((lcm_nm // N) -1) + ((lcm_nm // M) - 1)

# K番目の数がlcm_nmの何倍目に位置するか（0始まり）


k_multi = (K - 1) // cnt
k_pos = (K - 1) % cnt + 1
ans = 1
check = 0
while True:
  if ans % N == 0 or ans % M == 0:
    check += 1
  if check == k_pos:
    break
  ans += min(abs((ans % N) - N), abs((ans % M) - M))

print(ans + k_multi * lcm_nm)




# 考察
# 公倍数と公倍数の間の片方でしか割れない数の間隔は等しい

# 最小公倍数までの間にある、割れる数は求めることができてる。
# 結局求めるものは、K番目のものの数。
# どうやったら効率的？？