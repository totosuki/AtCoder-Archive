n = int(input())
for i in range(n,920):
  i = str(i)
  if int(i[0]) * int(i[1]) == int(i[2]):
    print(i)
    break