A, B, C = map(int, input().split())
is_plus = False
is_minus = False
if A+B == C:
  is_plus = True
if A-B == C:
  is_minus = True

if is_plus and is_minus:
  print("?")
elif is_plus:
  print("+")
elif is_minus:
  print("-")
else:
  print("!")