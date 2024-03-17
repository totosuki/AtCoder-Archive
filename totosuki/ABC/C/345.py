from string import ascii_lowercase
from bisect import bisect_left

S = list(input())
len_s = len(S)
memo = {s:[] for s in ascii_lowercase}

for i in range(len_s):
  memo[S[i]].append(i)

ans = 0

for i in range(len_s):
  until = len_s - i - 1
  id = bisect_left(memo[S[i]], i)
  ans += until - (len(memo[S[i]]) - id - 1)

for s in ascii_lowercase:
  if len(memo[s]) > 1:
    ans += 1
    break

print(ans)

# 97 = ord(a)

# S[i]よりあとにある同じ文字を引いた数が変えられるすべてのやつ
# それらを足し合わせたら答えかな