print('===Temperatre Lab ===')
celsius = float(input('Give Tempreature in Celsius:-'))
print('1. Change in farenheit 2. Change in Kelvin')
choice = input('Choice (1/2)\n:')

if choice == '1':
    farenheit = (celsius*9/5) + 32
    print(f'Temperature: {farenheit} F')
elif choice == '2':
    kelvin = celcius + 273.15
    print(f'Temperature: {kelvin} K')
else:
    print('Wrong Choice!\nPlease only chosse from options!')