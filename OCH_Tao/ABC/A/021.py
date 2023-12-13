N = int(input())
X = format(N,"04b")
i = 0
print(X.count("1"))
for bin in X:
  if bin == "1":
    print(2 ** (3 - i))
  i += 1