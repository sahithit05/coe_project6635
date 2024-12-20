def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_string =input("enter any string")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
