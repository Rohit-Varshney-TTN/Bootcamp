class InvalidPhoneError(Exception):
    pass
def check_phone(n):
    if len(n)!=10:
        raise InvalidPhoneError
    return True
try:
    n=input("Enter a 10-digit phone number: ")
    check_phone(n)
    print("Phone number is checked")
except InvalidPhoneError:
    print("Invalid phone no. Please enter all 10 digits")