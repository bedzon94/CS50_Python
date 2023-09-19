import inflect

#Set variable for inflect join function
p = inflect.engine()

#Initilize an empty list
names = []

#Loop forver
while True:
    try:
        #Prompt user for input
        name = input("Name: ")
        #Check if name is not in the list and append
        if name not in list(names):
            names.append(name)
        else:
             break

    except EOFError:
        #If user quits the program
        message = "Adieu, adieu, to "
        fun = p.join(list(names))
        print(message + fun)
        break

