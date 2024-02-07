A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in A:
  for j in B:
    if i == j:
      print("YES")
      break
  else:
    continue
  break
else:
  print("NO")