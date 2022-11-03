from validator_collection import validators, checkers, errors

def main():
    print(is_valid(input("What's your email address? ")))

def is_valid(s):
    is_email_address = checkers.is_email(s)

    if is_email_address == True:
        return "Valid"
    else:
        return "Invalid"

if __name__== "__main__":
    main()
