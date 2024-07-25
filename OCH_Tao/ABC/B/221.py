S = list(input())
T = input()
if "".join(S)==T:
  print("Yes")
else:
  for i in range(len(S)-1):
    S[i],S[i+1]=S[i+1],S[i]
    if "".join(S)==T:
      print("Yes")
      break
    else:
      S[i],S[i+1]=S[i+1],S[i]
  else:
    print("No")