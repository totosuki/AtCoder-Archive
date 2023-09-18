S = input()
T = input()

len_s = len(S)
len_t = len(T)

diff = set()

st_diff = len_s - len_t

for i in range(len_t):
  s, t = S[i + st_diff], T[i]
  if s == "?" or t == "?" or s == t:
    continue
  else:
    diff.add(i)

# x == 0
print("No") if diff else print("Yes")

for i in range(len_t):
  s, t = S[i], T[i]
  
  if s == "?" or t == "?" or s == t:
    if i in diff:
      diff.remove(i)
  else:
    diff.add(i)
  
  print("No") if diff else print("Yes")
