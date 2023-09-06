S = input()
s_len = len(S)
rslt = ""
for i in range(1, int((s_len / 2)) + 1):
  rslt += S[i*2-1] + S[i*2-2]
print(rslt)