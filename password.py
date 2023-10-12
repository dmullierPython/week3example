if __name__ == '__main__':
    password = input("enter your new password : ")
    special_characters = ["@", "_", "!", "#", "$", "%", "^", "&", "*", "~", ":"]
    numeric = False
    upper = False
    lower = False
    special_char = False
    length = False

    for c in password:
        if c.isnumeric():
            numeric = True
        if c.isupper():
            upper = True
        if c.islower():
            lower = True
        if c in special_characters:
            special_char = True
    print(len(password))
    if 8 <= len(password) <= 12:
        length = True

    if numeric is True and upper is True and lower is True and length is True and special_char is True:
        print("Password Check Result: Check ok")
    else:
        print("Password Check Result: Check failed")
