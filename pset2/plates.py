def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Chekcs if input is less than 2 cha or more than 6 cha and if first 2 cha != int and no punct allowed
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for letter in s:
            #If letters in the string is digit
            if letter.isdigit():
                #Store it's index in a variable called index
                index = s.index(letter)
                #Check if the last index of the input if its not digits and != 0
                if s[index:].isdigit() and letter != "0":
                    return True
                else:
                    return False
        return True


main()
