N = int(input())
A = []
for i in range(N):
  A.append(input())
for i in range(N):
  for j in range(i,N):
    if i==j:
      continue
    elif A[i][j]==A[j][i]=="D":
      continue
    elif A[i][j]!=A[j][i] and A[i][j]!="D" and A[j][i]!="D":
      continue
    else:
      print("incorrect")
      break
  else:
    continue
  break
else:
  print("correct")