import random
print('=== Welcome to no. gueesing game===')
print('guess a no. between 1 to 100')

secret_number = random.randint(1,100)
attempts=0

while True:
    guess= int(input('give your no. :-'))
    attempts +=1
    
    if guess<secret_number:
        print('Thoda bada number socho!')
        
    elif guess>secret_number:
        print('thoda small socho!')
        
    else:
        print(f"congratulations! You guess correect number {secret_number}")
        print(f"Apko {attempts} kosis lagi.")
        break