N = int(input())
W = list(input().split())
l = ["and", "not", "that", "the", "you"]
for text in W:
  for check_text in l:
    if text == check_text:
      print("Yes")
      exit()
print("No")