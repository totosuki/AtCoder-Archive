[[l.append(l[-1].replace(s,""))if s!=""else print("YNEOS"[l[-1]!=""::2])for s in ["ch","o","k","u",""]]for l in [[input()]]]
[[l.append(l[-1].replace(s,""))if s!=0 else print("YNEOS"[l[-1]!=""::2])for s in ["ch","o","k","u",0]]for l in[[input()]]]
[[l.append(l[-1].replace(s,""))if s else print("YNEOS"[l[-1]!=""::2])for s in ["ch","o","k","u",0]]for l in[[input()]]]
for l in[[input()]]:[l.append(l[-1].replace(s,""))if s else print("YNEOS"[l[-1]!=""::2])for s in ["ch","o","k","u",0]]

for l in[input().translate(str.maketrans("","","oku"))]:print("YNEOS"[l.replace("ch","")!=""::2])

# import re;print("YNEOS"[re.sub(r"ch|o|k|u", "", input())!=""::2])

# x = input()
# for c in ["ch","o","k","u"]:
#   x = x.replace(c, "")
# print("YES") if not x else print("NO")

# if not X: print("YNEOS"[bool(x)::2]) 
#   print("YES")
# elif X[-1] in "oku":
#   print("YES")
# elif X[-2:] == "ch":
#   print("YES")
# else:
#   print("NO")