from collections import Counter
N = int(input())
S = [input() for _ in range(N)]

counter = Counter(S)

for s in ["AC", "WA", "TLE", "RE"]:
  print(s + " x " + str(counter[s]))

# AC
# cnt_l = [0,0,0,0]

# for i in range(N):
#   S = input()
#   if S == "AC":
#     cnt_l[0] += 1
#   elif S == "WA":
#     cnt_l[1] += 1
#   elif S == "TLE":
#     cnt_l[2] += 1
#   else:
#     cnt_l[3] += 1

# print("AC x " + str(cnt_l[0]))
# print("WA x " + str(cnt_l[1]))
# print("TLE x " + str(cnt_l[2]))
# print("RE x " + str(cnt_l[3]))