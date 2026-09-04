def is_palindrome(str):
    return str==str[::-1]
name=input("enter a string")
if is_palindrome(name):
    print("palindrome")
else:
    print("not a palindrome")