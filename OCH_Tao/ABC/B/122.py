import re
S = input()
X = re.findall(r'[ACGT]*',S)
print(max([len(i) for i in X]))