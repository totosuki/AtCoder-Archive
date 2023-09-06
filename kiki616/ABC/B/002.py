import re
W = input()
cnt = re.split("[aiueo]",W)
an = ''
for i in cnt:
    an = an + i
print(an)