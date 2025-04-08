H,M = map(int,input().split())
while True:
  A = H//10
  B = H%10
  C = M//10
  D = M%10
  if A*10+C<24 and B*10+D<60:
    print(H,M)
    break
  else:
    M+=1
    if M==60:
      M=0
      H+=1
      if H==24:
        H=0