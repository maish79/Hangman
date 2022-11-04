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
words = random.choice(hangman_letters.word_list)

print(logo)

name = input("Enter your name:\n")
print("welcome",name,"!")
print("You have 6 attempts to guess the word!")

blank = []
for i in word:
    blank.append("_")

while not end_of_game:
    guess = input("Guess a letter:\n").lower()