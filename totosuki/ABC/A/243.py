V, A, B, C = map(int, input().split())
amari = V % (A+B+C)
if amari < A:
  print("F")
elif amari < A+B:
  print("M")
else:
  print("T")