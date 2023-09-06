d={}
for _ in[0]*int(input()):
  for i,s in enumerate(input()):
    s=int(s)
    try:
      while i in d[s]:i+=10
      d[s].add(i)
    except:d[s]={i}
print(min(max(d)for d in d.values()))