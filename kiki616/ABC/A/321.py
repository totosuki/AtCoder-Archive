N = input()
isis = True
for i in range(len(N)-1):
    if int(N[i]) <= int(N[i+1]):
        isis = False
if isis:
    print("Yes")
else:
    print("No")