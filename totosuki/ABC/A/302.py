A, B = map(int, input().split())
result = A // B
amari = A % B
if amari == 0:
  print(result)
else:
  print(result + 1)