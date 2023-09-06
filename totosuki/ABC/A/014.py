a = int(input())
b = int(input())
if a % b:
  print(b - (a % b))
else:
  print(0)



print(*[0 if i[0] % i[1] == 0 else i[1]-(i[0] % i[1]) for i in [[int(input()) for i in range(2)]]])

print(*[0 if i[0] % i[1] == 0 else i[1]-(i[0] % i[1]) for i in [[int(input()) for j in [1,1]]]])

print(*[0 if not i[0]%i[1] else i[1]-(i[0] % i[1]) for i in [[int(input()) for j in [1,1]]]])

print(*[i[1]-(i[0] % i[1]) if i[0]%i[1] else 0 for i in [[int(input()) for j in [1,1]]]])

print(*[i[1]-n if (n := i[0]%i[1]) else 0 for i in [[int(input()) for j in [1,1]]]])

for i in [[int(input()) for _ in [1,1]]]:print(i[1]-n if (n := i[0]%i[1]) else 0)

for i in[[int(input())for _ in[1,1]]]:print(i[1]-n if(n:=i[0]%i[1])else 0)

for i in[[int(input())for _ in[1,1]]]:print((i[1]-i[0]%i[1])%i[1])

print(b-a%b if(a:=int(input()))%(b:=int(input()))else 0)

print((a:=int(input()))%(b:=int(input()))and b-a%b or 0)

x,y=int(input()),int(input());print((y-x%y)%y)

x,y=int(input()),int(input());print(-x%y%y)

a=int(input());b=int(input());print(b-(a%b)if a%b else 0) # 違法ワンライナー




