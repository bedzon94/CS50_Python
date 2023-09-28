def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for letter in s:
            if letter.isdigit():
                index = s.index(letter)
                if s[index:].isdigit() and letter != "0":
                    return True
                else:
                    return False
        return True
    return False

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> refs/remotes/origin/main
