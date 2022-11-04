hangman = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=======''','''
 +---+
 |   |
 O   |
/|\  |
  \  |
     |
=======''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=======''','''

+---+
 |   |
 O   |
/|   |
     |
     |
=======''','''

+---+
 |   |
 O   |
 |   |
     |
     |
=======''','''


+---+
 |   |
 O   |
     |
     |
     |
     |
=======''','''

+---+
 |   |
     |
     |
     |
     |
=======''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | 
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import random
import hangman_letters
 
 #variables
a = set("abcdefghijklmnopqrstuvwxyz")
lives = 6
guessed = " "
end_of_game = False
word = random.choice(hangman_letters.word_list)

print(logo)

name = input("Enter your name:\n")
print("welcome",name,"!")
print("You have 6 attempts to guess the word!")

blank = []
for i in word:
    blank.append("_")

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

# making sure player chooses a letter not already guesssed
    
    if len(guess) > 1:
        print("Please pick a single letter.")
        
    elif guess not in a:
        print("Please make sure enter a letter.")
        
    elif guess in guessed:
        print(f'You already guessed the letter {guess}, please try again.')


    guessed += guess
    # main  loop 
    # checks to see if guess is in the word
    if guess in word:
        int = 0
        for i in word:
            if i == guess:
                blank[int] = guess
                int += 1
            else:
                int += 1
        print(blank)
        print(hangman[lives])
    else:
        print(f"Sorry, {guess} is not in the word. Try again!")
        print(blank)
        lives -= 1
        print(hangman[lives])
        
     # checking to see if the player guessed the  word
    if "_" not in blank:
        print("Congratulations, you win!")
        end_of_game = True
    
    # checking to see if the user lost. 
    if lives == 0:
        print("You lose!")
        print("The word was " + word)
        end_of_game = True