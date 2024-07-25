N = int(input())
L = []
for i in range(N):
  S,T = input().split()
  L.append({"S":S,"T":int(T)})
L.sort(key=lambda x:x["T"],reverse=True)
print(L[1]["S"])