for i in range(8, 0, -1):
  S = input()
  if "*" in S:
    print(f"{chr(S.index('*')+97)}{i}")
