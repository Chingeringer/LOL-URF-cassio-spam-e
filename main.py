import keyboard

import time
import random

    
    

if __name__ == "__main__":#hold to spam
    pressing = False
    while True:  # making a loop
        time.sleep(random.expovariate(lambd=5))
        if keyboard.is_pressed('space') and pressing == False:  # if key 'q' is pressed 
            pressing = True
            keyboard.press_and_release('e')#spam key
        if keyboard.is_pressed('space') and pressing == True:
            pressing = False
        if keyboard.is_pressed('o'):
            exit()
