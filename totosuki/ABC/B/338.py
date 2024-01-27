import string

S = input()
cnt = {}

for char in string.ascii_lowercase:
  cnt[char] = 0

for s in S:
  cnt[s] += 1

ans = ""
x = 0

for k, v in cnt.items():
  if v > x:
    ans = k
    x = v

print(ans)


