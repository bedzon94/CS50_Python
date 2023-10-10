import validators

def main():
    email = input("What's your email address? ")
    email_validator(email)


def email_validator(text):
    checker = validators.email(text)
    if checker:
        print("Valid")
    else:
        print("Invalid")




if __name__ == "__main__":
    main()
