N = int(input())
A = list(map(int,input().split()))
isis = 0
for i in range(N):
    for l in range(N):
        for j in range(N):
            if not(i==l or i==j or j==l):
                if A[i]+A[l]+A[j]==1000:
                    isis = 1
print("Yes"if isis else "No")