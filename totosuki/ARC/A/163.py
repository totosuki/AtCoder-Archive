T = int(input())

for _ in range(T):
  N = int(input())
  S = input()
  answer = "No"  

  for i in range(1, N):
    if S[:i] < S[i:]:
      answer = "Yes"
  
  print(answer)