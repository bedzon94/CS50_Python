#Takes prompt from user
expression = input("Expression: ")

#Splits input into 3 variables
x, y, z = expression.split(" ")

#Converts first and lasy variables into int
a = int(x)
b = int(z)

#Engine works for the program
if y == "+":
    print(float(a + b))
elif y == "-":
    print(float(a - b))
elif y == "*":
    print(float(a * b))
elif y == "/":
    print(float(a / b))
else:
    print("Irregular Expression")
