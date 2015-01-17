#Text-adventure prototype 1.0

import time

time.sleep(1)
print ('Your eyes slowly open... an old man stands over you.')

time.sleep(1)
print ('"Why hello my friend, what might your name be?"')
name = input('Enter your name:')

time.sleep(1)
print ('"Ah,',name)
print ('a good name... there was a hero named ',name,' a long time ago."')

time.sleep(1)
print ('The old man sits you up.')
print ('You are in a clay hut, and there are shelves on the walls that are filled with different colored potions.')

time.sleep(1)
print ('"I found you in your burnt farm house, after you got raided by those nasty')
print (' barbaric thieves."')

def question1():
    print ('"Well, I\'m very sorry... how do you feel?')

def remember():
    rememberance = input('Do you remember this? Y/N:')
    if rememberance == 'y':
        question1()
    elif rememberance == 'n':
        print ('"Ah, well... the riders torched your barn and killed your livestock... then they plundered your house."')
        question1()
    else:
        print ('"What was that you said?"')
        remember()
remember()
