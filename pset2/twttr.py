#Variable list to be used to compare input

vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

user_input = input("Input: ")

#Translate method checks whether each char in the str is vowel and replaces it with None

user_input = user_input.translate({ord(i): None for i in vowels})

print(f"Output: {user_input}")







