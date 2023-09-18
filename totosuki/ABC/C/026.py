N = int(input())
B = [int(input()) for _ in range(N-1)]

def fun(n: int):
  member = [i for i in range(len(B)) if B[i] == n]
  
  if not member:
    return 1
  else:
    rslt = []
    for i in range(len(member)):
      rslt.append(fun(member[i]+2))
    return max(rslt) + min(rslt) + 1

print(fun(1))