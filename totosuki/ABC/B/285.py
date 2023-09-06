N = int(input())
S = input()
flag = False
for i in range(1, len(S)):
  flag = False
  for j in range(len(S) - i):
    i_1 = j
    i_2 = j+i
    if S[i_1] == S[i_2]:
      print(j)
      flag = True
      break
  
  if not flag:
    print(len(S) - i)