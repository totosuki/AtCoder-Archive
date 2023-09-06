S = input()[:-1]
while True:
  if len(S) % 2:
    S = S[:-1]
  else:
    half = len(S) // 2
    if S[:half] == S[half:]:
      print(len(S))
      break
    else:
      S = S[:-2]
