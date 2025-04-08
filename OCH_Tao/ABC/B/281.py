import re
S = input()
print("Yes" if re.fullmatch(r"[A-Z][1-9]\d{5}[A-Z]",S) else "No")