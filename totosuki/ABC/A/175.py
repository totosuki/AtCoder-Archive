S = input()
if S == "RRR":
  print(3)
elif S[0]+S[1] == "RR" or S[1]+S[2] == "RR":
  print(2)
elif "R" in S:
  print(1)
else:
  print(0)