S = input()
count = 0
count_ls = []
for i in range(len(S)):
  if i % 2 == 0 and S[i] != "0":
    count += 1
  elif i % 2 == 1 and S[i] != "1":
    count += 1
count_ls.append(count)
count = 0
for i in range(len(S)):
  if i % 2 == 0 and S[i] != "1":
    count += 1
  elif i % 2 == 1 and S[i] != "0":
    count += 1
count_ls.append(count)
print(min(count_ls))