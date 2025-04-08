L,R = map(lambda x:bool(int(x)),input().split())
print("Yes" if L and not R else "No" if not L and R else "Invalid")