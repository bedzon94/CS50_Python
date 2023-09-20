#Variable list to be used to compare input

vowels = ["a","e", "i", "o", "u"]

text = ""

user_input = input("Input: ")

for i in range(len(user_input)):
    if user_input[i].lower() not in vowels:
        text += user_input[i]
        
print(f"Output: {text}")

