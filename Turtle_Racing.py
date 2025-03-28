#Name: Turtle Racing Game
#Discription: User input the number of turles for the game. The first turtle reaches the line first will be a winner. 

import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'pink', 'brown', 'black', 'yellow', 'purple', 'gray']
def get_number_of_racers():
    racers = 0
    while True: 
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric.. Try Again!!!')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else: 
            print('Number is not in range 2-10. Try Again!!')
    
def race(colors):
    turtles = create_turtles(colors)
    
    while True: 
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    
        
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors): #enumerate is a counter item in a list and it will loop though all of the index in the list, start with the first index. 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
        
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!!!')
                        
racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
Colors = COLORS[:racers]

winner = race(Colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
turtle.done()