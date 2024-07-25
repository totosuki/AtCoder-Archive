P = list(map(int,input().split()))
print(*map(lambda x:chr(x+96),P),sep="")