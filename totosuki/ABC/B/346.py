key = "wbwbwwbwbwbw" * 100

W, B = map(int, input().split())
sm = W + B
ans = "No"

for i in range(150):
  wcnt = key[i:i+sm].count("w")
  bcnt = key[i:i+sm].count("b")
  if wcnt == W and bcnt == B:
    ans = "Yes"
    break

print(ans)