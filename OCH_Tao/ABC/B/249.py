from re import search
S = input()
print("Yes" if search(r"[A-Z]",S) and search(r"[a-z]",S) and len(S)==len(set(list(S))) else "No")