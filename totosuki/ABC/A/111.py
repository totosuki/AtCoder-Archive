print(input().translate(str.maketrans("19","91")))
print(input().translate(str.maketrans({"1":"9","9":"1"})))
print(input().replace("1","_").replace("9","1").replace("_","9"))