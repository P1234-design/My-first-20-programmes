print('   The Unknown Planet Adventure   ')
print('Your spaceship crashed on a unknown planet.')
print('You have only two way: "Forest" or "Cave".')
way = input('Where you want to go?\n:').lower()
if way == 'forest':
    print('In Forest there was a ALIEN.')
    action1 = input('Would you want to Run or Chat with alien.\n:')
    if action1 == 'chat':
        print('Alien become your Feiend(it is alien language on earth it is friend).And he take you and TUMHE AAJ KA DINNER BNA KE KHA GAYA!!!.GAME OVER!!!')
    else:
        print("when you run the alien will gir gaya in gaddha and you are not safe because the alein know how to jump !!!! HA HA HA .Now you will die.GAME OVER!!")
elif way == 'cave':
    print("In cave some sounds are comes.")
    action2 = input("You have a torch .Would you want to on this YES or NO.\n:-")
    if action2 == 'yes':
        print('You see there was a portal ,You not what is in it .')
        action3 = input("Enter or not enter\n:")
        if action3 == 'enter':
            print('When you enter in wormhole this open on black hole and you DIE!!!!!!!!!!!!!!.GAME OVER.')
        else:
            print('You terrified and not go bcz kam se kam yha zinda toh hai and one rescue space ship come and save you.')
    if action2 == 'no':
        print('One space mice come there and eat you.GAME OVER!!')
    

    
        