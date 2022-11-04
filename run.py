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
| | | | (_| | | | | (_| | | | | | | (_| | | | |
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
