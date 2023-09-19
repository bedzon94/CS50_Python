#Print statement before the prompt to the user
print("Amount Due: 50")

#Variables for the program
amount_due = 50
inserted_coin = 0

while True:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_due -= coin
        inserted_coin += coin

    if inserted_coin >= 50:
        print(f"Change Owed: {inserted_coin - 50}")
        break
    else:
        print(f"Amount Due: {amount_due}")
