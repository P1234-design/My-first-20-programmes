print('===Prime number Detecter===')
num = int(input('Give your number:- '))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(f'The {num} is not a Prime Number.')
            print(f'Because {num} is divisible by {i}.')
            break
    else:
         print(f'{num} is a Prime Number. ')
            
else:
    print('{num} cannot be a Prime Number.')