- Project name: Quiz Game 
- Description: Answer 10 simple quiz questions about the computer. 

print("Welcome to my quiz game!")

playing = input("Do you want to play? ")    #Then create a variable for playing

if playing.lower() != "yes":       #If statement doesn't equal to yes - then quit
    quit()                  # != means not equal to. 
print("Okayyy! Let's play :) ")
Score = 0 

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct !!!!')
    Score += 1                     #If the answer is correct, will get 1 point
else: 
    print('Incorrect')
    print('Try again!!!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct !!!!')
    Score += 1 
else: 
    print('Incorrect')
    print('Try again!!!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct !!!!')
    Score += 1 
else: 
    print('Incorrect')
    print('Try again!!!')


answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print('Correct !!!!')
    Score += 1 
else: 
    print('Incorrect')
    print('Try again!!!')

print("You got " + str(Score) + " questions correct!")
print("You got " + str((Score / 4) * 100) + "%")



