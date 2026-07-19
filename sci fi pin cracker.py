import time
import random

print(" !!! System Acces Terminal !!!")
target_pin = input("Set a three digit pin:  ")
print("Start Brute Force Hacking...")
time.sleep(2)
guess = "000"
attempts = 0

while guess != target_pin:
    guess = str(random.randint(0,999)).zfill(3)
    print(f"Trying Pin :{guess}")
    attempts += 10
    time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000002)
    
print(f">>ACCESS GRANTED ! PIN {guess} found in {attempts} attempts.")