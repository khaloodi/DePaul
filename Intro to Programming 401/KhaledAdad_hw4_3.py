# Khaled Adad

def main():
    pswrd = input("Enter password string: ")
    print(valid_password(pswrd))

def valid_password(pswrd):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    if len(pswrd) < 7:
        return False
        
    lowerCheck = upperCheck = digitCheck = False

    for char in pswrd:
        if (char in uppercase_letters):
            lowerCheck = True
        if (char in lowercase_letters):
            upperCheck = True
        if (char in digits):
            digitCheck = True

    if lowerCheck and upperCheck and digitCheck:
        return True 
    else:
        return False

main()