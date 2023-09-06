_ = int(input())
S = input()
ST = ["T" for s in S if s in "T"]
SA = ["A" for s in S if s in "A"]
if len(ST) > len(SA):
  print("T")
elif len(ST) < len(SA):
  print("A")
else:
  if S[len(S) - 1] == "T":
    print("A")
  else:
    print("T")