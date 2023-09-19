#Create an item dict
item_list = {}

while True:
    try:
        #Ask for item and convert to upper case
        item = input().upper()
        #See if item is in dict
        if item in item_list:
            #If yes add more of the same item
            item_list[item] += 1
        else:
            #If not then initialize item
            item_list[item] = 1
    #When done with shopping list ctrl + d
    except EOFError:
        #Sort the item list input for the user
        for output in sorted(item_list):
            #Print the list with number of entries
            print(item_list[output], output)
        break
