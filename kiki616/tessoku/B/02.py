A,B = map(int,input().split())
isis = 0
for i in range(A,B+1):
    if 100 % i == 0:
        isis = 1
print("Yes"if isis else "No")