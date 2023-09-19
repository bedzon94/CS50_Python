#Function that prompts for user input
def convert():
    word = input("What is your input: ")

    #Replaces :) with smiley face
    sub = word.replace(":)", "🙂")

    #Replaces :( with forwney face
    final = sub.replace(":(", "🙁")
    print(final)

def main():
    convert()


main()
