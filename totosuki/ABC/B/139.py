A, B = map(int, input().split())
cnt = 0
B -= 1

while B > 0:
  B += 1
  B -= A
  cnt += 1

print(cnt)