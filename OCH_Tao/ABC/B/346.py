W,B = map(int,input().split())
S = "wbwbwwbwbwbw"*20
for i in range(240-(W+B)):
  X = S[i:i+(W+B)]
  if X.count("w")==W and X.count("b")==B:
    print("Yes")
    break
else:
  print("No")