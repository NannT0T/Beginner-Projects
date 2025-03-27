#Name: Choose Your Own Adventure
#Discription: Create an advanture game for user to play. In the game, user can choose left or right to continute playing the game, and overcome the challenges at the end of each road. 


name = input("Type your name: ").lower() 
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else: 
        print('Not a valid option. You lose.')


elif answer == "right": 
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes": 
            print("You talked to the stranger and they gave you gold. YOU WIN!!!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. YOU LOSE.")
        else: 
            print('Not a valid option. You lose')
            
    else: 
        print('Not a valid option. You lose')

else: 
    print('Not a valid option. You lose.')

print ('Thank {name}, for participating to the game.'.format(name=name))
print('See you next time')
