import re
for _ in range(int(input("Enter number of Test cases:"))):
    s = input("Enter string: ")
    up = re.findall(r"[A-Z]",s)
    lo = re.findall(r"[a-z]",s)
    print("Total lowercase letters:", len(lo))
    print("Total uppercase letters:", len(up))