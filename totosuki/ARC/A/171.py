T = int(input())

for _ in range(T):
  N, A, B = map(int, input().split())
  row = N - A
  col = N - A
  
  # pone = row * colになるライン
  line = N // 2
  
  if A == 0:
    if row % 2 == 0:
      pone = col * (row // 2)
    else:
      pone = col * (row // 2 + 1)
  else:
    if A >= line:
      pone = row * col
    else:
      pone = col * A
      tmprow = (N - (A*2)) 
      if tmprow % 2 == 0:
        pone += col * (tmprow // 2)
      else:
        pone += col * (tmprow // 2 + 1)
  
  # print(f"pone:{pone}, line: {line}")
  
  if row < 0:
    print("No")
  elif B <= pone:
    print("Yes")
  else:
    print("No")
