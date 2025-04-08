S = input()
T = input()
if S == T:
  print(0)
else:
  for i in range(max(len(S), len(T))):
    try:
      if S[i] != T[i]:
        print(i+1)
        break
    except IndexError:
      print(i+1)
      break
