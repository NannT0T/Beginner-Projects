#Name: Alarm Clock
#Discription: Set-up an alarm sound with elapsing time inside the terminal. 

from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #the alarm will wait for 1s
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm wil sound in: {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("Alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds      
alarm(total_seconds)