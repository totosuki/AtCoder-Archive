S = list(map(lambda x:ord(x)-97,list(input())))
T = list(map(lambda x:ord(x)-97,list(input())))
diff = S[0]-T[0]
for i in range(len(S)):
  if (S[i]-diff)%26!=T[i]:
    print("No")
    break
else:
  print("Yes")