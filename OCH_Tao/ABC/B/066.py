S = input()
for i in range(2,len(S),2):
  if S[0:(len(S)-i)//2]==S[(len(S)-i)//2:len(S)-i]:
    print(len(S)-i)
    break