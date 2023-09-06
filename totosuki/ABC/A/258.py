K = int(input())
hh = ""
if K >= 60:
  hh = "22"
  K = K - 60
else:
  hh = "21"
print(hh + ":" + str(K).zfill(2))