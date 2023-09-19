#Main function calls snake_case
def main():
    case = input("camelCase: ")
    case = print("snake_case: ", snake_case(case))

#Function that outputs in put as snake_case
def snake_case(case):
    div = ""
    for letter in case:
        if (letter.isupper()):
            div += "_" + letter.lower()
        else:
            div += letter
    return div[0:]


main()
