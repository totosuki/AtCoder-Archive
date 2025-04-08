N = int(input())
S = input()
for i in range(1,N):
  for j in range(N-i):
    if S[j]==S[j+i]:
      print(j)
      break
  else:
    print(N-i)