import re
x = "This is ankit"
y = "\w+"
regex = re.compile(y)
z = regex.findall(x)
if z:
    a = max(z, key=lambda word : len(word))
    print(f"Longest word is {a}")