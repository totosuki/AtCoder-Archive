H, W = map(int, input().split())
R, C = map(int, input().split())
count = 0
if R - 1 >= 1:
  count += 1
if R + 1 <= H:
  count += 1
if C - 1 >= 1:
  count += 1
if C + 1 <= W:
  count += 1
print(count)