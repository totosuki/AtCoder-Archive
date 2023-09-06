A,B = map(int, input().split())

if B - A == 1:
    if A % 3 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")

# if A + 1 == B or  A - 1 == B or  A + 3 == B or  A - 3 == B:
#     if A % 3 == 0 
    
#     or B % 3 == 0 or A % 3 == 1 or A % 3 == 1:
#         print("No")
#     elif :
#         print("Yes")
# else:
#     print("No")