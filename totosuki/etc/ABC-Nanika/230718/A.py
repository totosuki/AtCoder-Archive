H, W = map(int, input().split())
cnt = 0
for h in range(H):
  s = input()
  cnt += s.count("#")

print(cnt)