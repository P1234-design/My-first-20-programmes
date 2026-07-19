import random

print('Welcome! in my self made game!')
options=["rock","paper","scissors"]

while True:
    user_choice=input("write your choice (rock,paper or scissors) OR 'quit' for quit the game :- ").lower()
    
    if user_choice == 'quit':
        print('Game over. Thank you for playing!')
        break
    if user_choice not in options:
        print('wrong input! only write rock , paper or scissors.')
        continue
    
    comp_choice = random.choice(options)
    print(f"Computer choses : {comp_choice}")
    
    if user_choice == comp_choice:
        print('Result: Draw!')
        
        
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'paper' and comp_choice == "rock" ) or (user_choice == 'scissors' and comp_choice == 'paper' ):
        print("congratulations! you are winner.")
        
    else:
        print('You are loose!')