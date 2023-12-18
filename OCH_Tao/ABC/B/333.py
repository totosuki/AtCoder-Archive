S = input()
T = input()
L = 'ABCDE'
x = abs((L.find(S[0]))-(L.find(S[1])))
y = abs((L.find(T[0]))-(L.find(T[1])))
if x == y:
  print('Yes')
elif x == abs(y - 5):
  print('Yes')
else:
  print('No')