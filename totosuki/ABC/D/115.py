import sys
sys.setrecursionlimit(10*9)

def hamburger(n, x):
  if n == 0:
    if x == 1:
      return 1
    else:
      return 0
  
  median = (layers[n]+1) // 2

  if x < median:
    return hamburger(n-1, x-1)
  elif x == median:
    return patty_layers[n-1] + 1
  elif x > median:
    return patty_layers[n-1] + 1 + hamburger(n-1, x - median)


N, X = map(int, input().split())
layers = [1]
patty_layers = [1]

for i in range(N):
  layers.append(layers[i]*2 + 3)
  patty_layers.append(patty_layers[i]*2 + 1)

rslt = hamburger(N, X)
print(rslt)

# def hamburger(l): # l = level
#   if l == 0:
#     return "P"
#   else:
#     return "B" + hamburger(l-1) + "P" + hamburger(l-1) + "B"

# N, X = map(int, input().split())
# hamburger_rslt = hamburger(N)
# rslt = hamburger_rslt[:X]
# patty_count = 0
# print(rslt.count("P"))