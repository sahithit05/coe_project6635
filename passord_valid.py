def password_strength(password):
    if len(password) < 10 or len(password) > 15:
        return "Password should contain a minimum of 10 characters and a maximum of 15 characters."
    if not (any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password)):
        return "Password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
    if any(char.isspace() for char in password):
        return "Password should not contain white spaces."
    if password[-1] == '.' or password[-1] == '@':
        return "Password should not end with a dot (.) or '@' symbol."
    return "Password is correct."
password = input("Enter the password: ")
print(password_strength(password))