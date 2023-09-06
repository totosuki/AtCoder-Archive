def return_new_T(T):
  indexes = [i for i,T in enumerate(T) if T in "A"] + [i for i,T in enumerate(T) if T in "B"]
  new_T = [T[i + 1] for i in indexes if i < len(T) - 1]
  return new_T

times= int(input())
for time in range(times):
  n = int(input())
  T = input()
  print(T)
  for i in range(n - 1):
    new_T = return_new_T(new_T) if i != 0 else return_new_T(T)
  print(*new_T)