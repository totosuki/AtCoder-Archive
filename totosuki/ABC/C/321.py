K = int(input())

numbers = []

for a in range(10):
  numbers.append(a)

for b in range(10):
  for a in range(b):
    numbers.append(b*10 + a)

for c in range(10):
  for b in range(c):
    for a in range(b):
      numbers.append(c*100 + b*10 + a)

for d in range(10):
  for c in range(d):
    for b in range(c):
      for a in range(b):
        numbers.append(d*1000 + c*100 + b*10 + a)

for e in range(10):
  for d in range(e):
    for c in range(d):
      for b in range(c):
        for a in range(b):
          numbers.append(e*10000 + d*1000 + c*100 + b*10 + a)

for f in range(10):
  for e in range(f):
    for d in range(e):
      for c in range(d):
        for b in range(c):
          for a in range(b):
            numbers.append(f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)

for g in range(10):
  for f in range(g):
    for e in range(f):
      for d in range(e):
        for c in range(d):
          for b in range(c):
            for a in range(b):
              numbers.append(g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)

for h in range(10):
  for g in range(h):
    for f in range(g):
      for e in range(f):
        for d in range(e):
          for c in range(d):
            for b in range(c):
              for a in range(b):
                numbers.append(h*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)

for i in range(10):
  for h in range(i):
    for g in range(h):
      for f in range(g):
        for e in range(f):
          for d in range(e):
            for c in range(d):
              for b in range(c):
                for a in range(b):
                  numbers.append(i*100000000 + h*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)

for j in range(10):
  for i in range(j):
    for h in range(i):
      for g in range(h):
        for f in range(g):
          for e in range(f):
            for d in range(e):
              for c in range(d):
                for b in range(c):
                  for a in range(b):
                    numbers.append(j*1000000000 + i*100000000 + h*10000000 + g*1000000 + f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)

print(numbers[K])