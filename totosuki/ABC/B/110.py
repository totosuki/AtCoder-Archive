N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
answer = "War"

for Z in range(X+1, Y+1):
  flag = False
  for i in range(len(x)):
    if x[i] >= Z:
      flag = True
  for i in range(len(y)):
    if y[i] < Z:
      flag = True
  
  if not flag:
    answer = "No War"

print(answer)