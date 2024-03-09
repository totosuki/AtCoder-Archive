s = list(input())
diff = list(set(s))
a = s.count(diff[0])
b = s.count(diff[1])

if a < b:
  c = diff[0]
else:
  c = diff[1]

cnt = 0

for i in range(len(s)):
  if s[i] == c:
    print(i+1)
    exit()