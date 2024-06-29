import math

MOD = 10**9 + 7

N = int(input())
S = input()

i = 1
now = S[0]
ans = 1
while i < N:
  if now == S[i]:
    i += 1
    continue
  else:
    cnt = 1
    while i < N and now != S[i]:
      now = S[i]
      i += 1
      cnt += 1
    ans *= math.ceil(cnt / 2)
    ans %= MOD

print(ans)

# ABABABとかは必ずABABになる


# BBABABAABABAAAABA
# B BABA ABABAAAABA
# B  BA  ABABAAAABA
# BBABABA AB