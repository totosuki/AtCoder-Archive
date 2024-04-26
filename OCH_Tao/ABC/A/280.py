H,W = map(int,input().split())
cnt = 0
for i in range(H):
  cnt+=input().count("#")
print(cnt)