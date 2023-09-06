A, B, C, D, E, F, X = map(int, input().split())
t_span = A + C
t = ((X//t_span) * A * B)
t_nokori = X % t_span
if t_nokori <= A:
  t += t_nokori * B
else:
  t += A*B

a_span = D + F
a = ((X//a_span) * D * E)
a_nokori = X % a_span
if a_nokori <= D:
  a += a_nokori * E
else:
  a += D*E

if t > a:
  print("Takahashi")
elif t < a:
  print("Aoki")
else:
  print("Draw")