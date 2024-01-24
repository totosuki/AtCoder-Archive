S = input()
l = []
l.append(S.count("A"))
l.append(S.count("B"))
l.append(S.count("C"))
l.append(S.count("D"))
l.append(S.count("E"))
l.append(S.count("F"))
print(" ".join(str(i) for i in l))