import time

print('SPACESHIP LAUNCH SEQUENCE')
seconds = int(input('How much second countdown you want?\n :- '))

while seconds >-1 :
    print(f"T-Minus: {seconds} seconds")
    time.sleep(1)
    seconds -= 1
   
if seconds := 1:
    print('!!!!Countdown over !!!! \n Spaceship IGNITION! LIFT OFF! ')