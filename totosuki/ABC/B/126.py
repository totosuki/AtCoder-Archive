S = input()
answer = "NA"

if 1 <= int(S[:2]) <= 12 and 1 <= int(S[2:]) <= 12:
  answer = "AMBIGUOUS"
elif 1 <= int(S[2:]) <= 12:
  answer = "YYMM"
elif 1 <= int(S[:2]) <= 12:
  answer = "MMYY"

print(answer)