word = "SCIENCE"
gussed_word = ["_"] * len(word)

print('Find the word : ' + " ".join(gussed_word))

while "_" in gussed_word:
    guess = input('Guess a letter :').upper()
    if guess in word:
        for i in range (len(word)):
            if word[i] == guess:
                gussed_word[i] = guess
            print('Sahi! ' + ' '.join(gussed_word))
            
    else:
        print('Wrong guess!')
        
        
print('mission accomplished')