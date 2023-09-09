N = int(input())
jl = []
ans = ""
for i in range(1,10):
    if N % i == 0:
        jl.append(i)
for i in range(N+1):
    b = []
    for k in range(2000):
        for j in jl:
            if N/j * k == i:
                b.append(j)
    if b:
        ans = ans+str(min(b))
    else:
        ans = ans+"-"
print(ans)