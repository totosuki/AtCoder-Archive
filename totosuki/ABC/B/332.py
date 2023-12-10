K, G, M = map(int, input().split())
gurasu = 0
magu = 0

for _ in range(K):
  if gurasu == G:
    gurasu = 0
  elif magu == 0:
    magu = M
  else:
    amari = G - gurasu
    if amari >= magu:
      gurasu += magu
      magu = 0
    else:
      gurasu = G
      magu = magu - amari

print(gurasu, magu)