N, K, A = map(int, input().split())
pos = A
for _ in range(K-1):
  pos += 1
  if pos > N:
    pos = 1
print(pos)