w = input()
w_nodupe = list(set(w))
for t in w_nodupe:
  if w.count(t) % 2:
    print("No")
    exit()
print("Yes")