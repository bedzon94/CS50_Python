#Initiate a forver loop that prompts user
while True:
    get_fra = input("Fraction: ")
    try:

        #Split input into numerator(x) and denominator(y)
        x, y = get_fra.split("/")

        #Convert str into int
        x = int(x)
        y = int(y)
        div = x / y

        #Break out of the forver loop if this condition is met
        if div <=1:
            break
    #Handle ValueError and ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        pass

#Round result of % and check conditions
result = round(div * 100)
if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")



