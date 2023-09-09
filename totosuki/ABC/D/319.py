def can_fit(words, W, M):
  lines = 1
  now_w = 0

  if words[0] > W:
    return False

  for word in words:
    if now_w + word > W:
      lines += 1
      now_w = word + 1
      if now_w - 1 > W:
        return False
    else:
      now_w += word + 1

  return lines <= M

N, M = map(int, input().split())
L = list(map(int, input().split()))

left, right = 0, sum(L) + N + 3

while right - left > 1:
  mid = (left + right) // 2

  if can_fit(L, mid, M):
    right = mid
  else:
    left = mid

print(right)