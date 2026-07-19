import time
print("Prasant ke banaye calculator mein apka swagat hai")
num1= float(input("give me first no.:"))
operator=input ("what do you want to do? (+,-,*, /  tell):")
num2= float(input("give me second no.:"))

if operator == '+':
    result= num1 +num2
    print("your ans is:",result)
elif operator == '-':
    result= num1 -num2
    print("your ans is:",result)
elif operator == '*':
    result= num1*num2
    print("your ans is:",result)
elif operator == '/':
    if num2 ==0:
        print ("Eroor:it is undefinate form!")
    else:
        result= num1/num2
        print("your ans is:",result)
        time.sleep(3)
while True:
    print('\nMain Menu:-')
    print('1. Calculator')
    print('2. For find square root.')
    print('3. close the programme')
    
    choice = input('Give your choice (1/2/3):-')
    
    if choice == '1':
        num1= float(input("give me first no.:"))
        operator=input ("what do you want to do? (+,-,*, /,tell):")
        num2= float(input("give me second no.:"))  
    if operator == '+':
        result= num1 +num2
        print("your ans is:",result)
    elif operator == '-':
        result= num1 -num2
        print("your ans is:",result)
    elif operator == '*':
        result= num1*num2
        print("your ans is:",result)
    elif operator == '/':
        if num2 == '0':
            print ("Error:it is undefinate form!")
        else:
            result= num1/num2
            print("your ans is:",result)
            time.sleep(3)
    if choice == '2':
        num = float(input('Give number whose square root is to be find:'))
        print('Square root of ',num,'is :',num**0.5)
        time.sleep(3)
    if choice == '3':
        print("Program is closing.Bye!")
        break

else:
    print('Wrong choice!\nPlease choose only from given options.')
 
time.sleep(3)       

    
   