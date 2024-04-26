S = input()
L = []
for i in range(len(S)-2):
  L.append(int(S[i:i+3]))
diff = [abs(753-x) for x in L]
print(min(diff))