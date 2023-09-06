S = input()
rslt = 999

for i in range(len(S)-2):
  X = int(S[i:i+3])
  rslt = min(rslt, abs(X - 753))

print(rslt)