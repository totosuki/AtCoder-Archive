S = input()
print(S[::-1].translate(str.maketrans({"6":"9","9":"6"})))