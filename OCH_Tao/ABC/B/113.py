N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
L = []
for i in H:
  L.append(abs(A-(T-i*0.006)))
print(L.index(min(L))+1)