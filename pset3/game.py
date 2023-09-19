import random

#Loop forver
while True:
    try:
        #Get user input and exit this loop when input is positive int
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

#Get a random int from level input
rand_int = random.randint(1, level)
#Start a forver loop
while True:
    try:
        #Get guess input from user
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < rand_int:
                print("Too small!")
            elif guess > rand_int:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
         pass

