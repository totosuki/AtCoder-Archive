import re
S = input()
l = re.findall(r'A[A-Z]*Z',S)
print(max(list(map(len,l))))