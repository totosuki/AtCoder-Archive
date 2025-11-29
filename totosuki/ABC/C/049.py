from collections import deque

S = deque(input())
words = {"dream", "dreamer", "erase", "eraser"}
cache = ""
ans = True


for _ in range(len(S)):
    t = S.pop()
    cache = t + cache
    if cache in words:
        cache = ""
    if len(cache) > 7:
        break

if cache:
    ans = False

print("YES" if ans else "NO")
