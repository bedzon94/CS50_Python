#Have a menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#Initialize order total
order_total = 0
#Loop forever
while True:
    try:
        #Get user input (convert to titlecase)
        item = (input("Item: ")).title()
        #Check if input in menu
        if item in menu:
            #If yes then add the price of item to order_total
            order_total += menu[item]
            #Print order total and continue
            print("Total: ${:.2f}".format(order_total))
        else:
            print("Total: ${:.2f}".format(order_total))
    #Handle ctrl + d as done
    except EOFError:
        print()
        break
