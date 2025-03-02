# Project name: Number guessing game
# Description: The user inputs a number to generate a random number for the guessing game. Next, they must guess the random number to win; otherwise, they can keep trying. 


import random              # Imported a random module. 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print("Please type a number larger than 0 next time.")
        quit()

else: 
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)          
guesses = 0

while True: 
    guesses += 1 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!!!!!")
        break
    elif user_guess > random_number: 
        print("You were above the number!")
    else: 
        print("You were below the number!")


print("You got it in", guesses, "guesses")      #We can use either , or + for the print statement. 
                                                #When we use comma, we don't need to add str for guesses
