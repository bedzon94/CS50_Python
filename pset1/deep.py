#Takes user input
question = input("What is the Great Question of Life, the Universe and Everything? ")

#Converts to lower case and strips whitspace
query = (question.lower()).strip()
if query == "42" or query == "forty-two" or query == "forty two":
        print("Yes")
else:
    print("No")
