X = input()
answer = "Strong"

if X[:2] == X[2:]:
  answer = "Weak"

for i in range(3):
  x = int(X[i])
  y = int(X[i+1])
  if x+1 == y:
    continue
  elif x == 9 and y == 0:
    continue
  else:
    break
else:
  answer = "Weak"

print(answer)