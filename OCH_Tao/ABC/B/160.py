X = int(input())
cnt = X//500*1000
X = X%500
print(cnt+X//5*5)