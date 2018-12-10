ia = input("Enter a word to check if it is palindrome : ")
x = a[::-1]
if a != x:
    print(f"Palindrome of {a} is {x}")
else:
    print("Not a palindrome")
