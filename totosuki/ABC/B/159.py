S = input()
answer = "Yes"

# 1
kaibun = "".join(reversed(list(S)))
if S != kaibun:
  answer = "No"

# 2
N = len(S)
end = (N - 1) // 2
kaibun = "".join(reversed(list(S[:end])))
if S[:end] != kaibun:
  answer = "No"

# 3
st = (N + 3) // 2
kaibun = "".join(reversed(list(S[st-1:])))
if S[st-1:] != kaibun:
  answer = "No"

print(answer)