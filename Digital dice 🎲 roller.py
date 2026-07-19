import random

print('DIGITAL DICE ROLLER')
print('For roll dice press enter or if you not want to roll then press "q" to quit.')

while True:
    user_input = input('Roll? or quit  ')
    if user_input.lower() == 'q':
        print('Game Over')
        break
    number = random.randint(1,6)
    print(f'After rolling the number comes on dice is: {number}')
