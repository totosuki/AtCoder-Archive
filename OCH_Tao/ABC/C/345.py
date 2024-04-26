#未AC TLE
S = input()
cnt = 0 if len(S)==len(set(list(S))) else 1
for i in range(len(S)-1):
  cnt+=(len(set(list(S[i+1:]))-set(S[i])))
print(cnt)