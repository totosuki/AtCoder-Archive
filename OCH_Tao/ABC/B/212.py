X = input()
S = "1234567890123"
print("Weak" if len(set(list(X)))==1 or X in S else "Strong")