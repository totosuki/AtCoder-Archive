s = input()
result = ""
for command in s:
  if command == "0":
    result += "0"
  elif command == "1":
    result += "1"
  elif command == "B":
    result = result[:-1]
print(result)