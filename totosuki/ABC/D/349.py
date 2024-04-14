def get_MSB(n):
  if n == 0:
    return 0
  msb = 1
  while n > 1:
    n = n >> 1
    msb = msb << 1
  return msb

L, R = map(int, input().split())

now = L
ans = []

while now < R:
  lsb = now & -now
  if now == 0:
    lsb = get_MSB(R)
  if now + lsb > R:
    break
  ans.append([now, now + lsb])
  now += lsb

while now < R:
  msb = get_MSB(R - now)
  ans.append([now, now + msb])
  now += msb


print(len(ans))
for a in ans:
  print(*a)

# 考察
# ビット関係の問題な気がする
# 2進数で考える
# S(3, 19)の場合、できるだけ大きいLSBになるようにしていけばいい。
# 3: 00000011
# 19: 00010011
# 3: 00000011 -> S(0, 3) = {3}
# 4~7: 00000100 -> S(2, 1) = {4, 5, 6, 7}
# 8~15: 00001000 -> S(3, 1) = {8, 9, 10, 11, 12, 13, 14, 15}
# 16~17: 00010000 -> S(1, 8) = {16, 17}
# 18: 00010010 -> S(0, 18) = {18}

# 0のときはRの