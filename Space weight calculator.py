print("INTERGALACTIC WEIGHT CALCULATOR ")
earth_weight= float(input('Write your weight on earth (in kg):- '))
print("Planets: 1.Moon 2.Mars 3.Jupiter 4. Black Hole (super gravity)")
while True:
    try:
        choice = input("Where you want to go (1/2/3/4)? \n:")
        if choice <='0':
            print("Please! give only from options.")
            continue
    except ValuError:
        print("ERROR! Please give only number ,your input is valid.")
            

if choice == '1':
    weight= earth_weight*0.165
    print(f"On Moon your weight is :- {weight:.3f}kg")
    
elif choice == '2':
    weight= earth_weight*0.377
    print(f"On Mars your weight is :- {weight:.3f}kg")
    
elif choice == '3':
    weight= earth_weight*2.34
    print(f"On jupiter your weight is :- {weight:.3f}kg (aap dab jayenge!)")
    
elif choice == '4':
    print("In Black Hole the gravity is infnite so weight also infinite, So you  are spaghettified !")
else:
    print("Space ship's navigation burst out! your input is wrong.")
