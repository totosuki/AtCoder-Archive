N = int(input())
S = input()
i = 0
rslt = ""
while i < N:
  if i+1 < N:
    if S[i]+S[i+1] == "na":
      rslt += "nya"
      i += 1
    else:
      rslt += S[i]
  else:
    rslt += S[i]
  
  i += 1
print(rslt)
