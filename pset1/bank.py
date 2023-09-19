#Takes user input, removes case sensitivity and strips whitespace
greeting = ((input("Greeting: ")).casefold()).strip()

#Conditional statement on requirements
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") or greeting.startswith("hello"):
    print("$20")
else:
    print("$100")
