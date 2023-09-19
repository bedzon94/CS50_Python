#Asks user for input
fruit = input("Item: ")

#Set of stored values from https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version
value = [
    {"item": "apple", "calories": "130"},
    {"item": "avocado", "calories": "50"},
    {"item": "banana", "calories": "110"},
    {"item": "cantaloupe", "calories": "50"},
    {"item": "grapefruit", "calories": "60"},
    {"item": "grapes", "calories": "90"},
    {"item": "honeydew melon", "calories": "50"},
    {"item": "kiwifruit", "calories": "90"},
    {"item": "lemon", "calories": "15"},
    {"item": "lime", "calories": "20"},
    {"item": "nectarine", "calories": "60"},
    {"item": "orange", "calories": "80"},
    {"item": "peach", "calories": "60"},
    {"item": "pear", "calories": "100"},
    {"item": "pineapple", "calories": "50"},
    {"item": "plums", "calories": "70"},
    {"item": "strawberries", "calories": "50"},
    {"item": "sweet cherries", "calories": "100"},
    {"item": "tangerine", "calories": "50"},
    {"item": "watermelon", "calories": "80"},
]

#Checks if user's input is in the set of dict and outputs it's calorie per serving
for v in value:
        if v["item"] == fruit.casefold():
            result = v["calories"]
            print(f"Calories: {result}", end="\n")
        else:
              print("", end="")
