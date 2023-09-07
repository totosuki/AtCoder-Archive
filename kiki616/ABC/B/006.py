n = int(input())
a = [0,0,1]
answer = 0
if n < 3:
    print(a[n-1])
else:
    for i in range(4,n+1):
        a.append(a[i-2] + a[i-3] + a[i-4])
    if a[-1] >= 10007:
        print(a[-1] % 10007)
    else:
        print(a[-1])