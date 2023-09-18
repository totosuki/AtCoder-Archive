S = input()
cnt = 0
zero = False

if len(S) == 1:
  if S[0] == "0":
    print(0)
  else:
    print(1)
else:
  for i in range(len(S) - 1):
    s = S[i]
    ns = S[i+1]
    
    if s != "+" and s != "*":
      if s == "0":
        zero = True
        
      if ns == "+":
        if not zero:
          cnt += 1
        zero = False
  else:
    if ns == "0":
      zero = True
    if not zero:
      cnt += 1
  
  print(cnt)