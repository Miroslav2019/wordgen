#Ajalle's Word Generator v0.1
#(c) 2018 by Ajalle Perfej
#This script generates words according to a scheme customizable
#in the constants list at the top.

import sys
import random as rnd

#Constants list can be modified.
VOWELS = 'aeiou'
CONS_1 = 'bdgkpt'   #fixed-duration consonants
CONS_2 = 'fhs'      #fixed-duration sibilants
CONS_3 = 'lmnrvz'   #variable duration consonants ('zzzzz' as one
                    #sound)
CONS_4 = 'cjqwx'    #variable-pronunciation consonants

#Used for choosing between consonant sets with random.random()
THRESHOLD = 0.39

#Filename to save wordlist
FILENAME = 'wordlist-2'

INTRO = '''
Ajalle's Word Generator v0.1
(c) 2018 by Ajalle Perfej
This Python 3 script generates words incrementally. Each
increment is made up of signs from a random choice of the
following:

1. vowel-consonant-vowel
2. vowel-consonant
3. consonant-vowel-consonant
4. consonant-vowel

At each increment you are asked if you want to stop incrementing.
If you do, you can choose to save the word or skip saving it,
then to build another word or to quit.
'''

#Script functions.

def choose_consonant_set():
    '''Chooses the consonant set. The probabilities are:
    CONS_1 - over THRESHOLD of over THRESHOLD
    CONS_2 - under THRESHOLD of over THRESHOLD
    CONS_3 - over THRESHOLD of under THRESHOLD
    CONS_4 - under THRESHOLD of under THRESHOLD
    '''
    if rnd.random() > THRESHOLD:
        if rnd.random() > THRESHOLD:
            return CONS_1
        return CONS_2
    else:
        if rnd.random() > THRESHOLD:
            return CONS_3
        return CONS_4

def choose_consonant(consonants):
    return rnd.choice(consonants)

def choose_vowel():
    return rnd.choice(VOWELS)

def build_sign():
    '''Selects two consonants from the same set and two vowels.
    Uses the following scheme for building a sign made up of
    both consonants and vowels:
    V1 + C1 + V2 (ex. "age") - over-over THRESHOLD
    V2 + C2      (ex. "ep")  - over-under THRESHOLD
    C2 + V2 + C1 (ex. "peg") - under-over THRESHOLD
    C1 + V1      (ex. "ga")  - under-under THRESHOLD
'''
    consonant_set = choose_consonant_set()
    consonant_1 = choose_consonant(consonant_set)
    consonant_2 = choose_consonant(consonant_set)
    vowel_1 = choose_vowel()
    vowel_2 = choose_vowel()

    if rnd.random() > THRESHOLD:
        if rnd.random() > THRESHOLD:
            return vowel_1 + consonant_1 + vowel_2
        return vowel_2 + consonant_2
    else:
        if rnd.random() > THRESHOLD:
            return consonant_2 + vowel_2 + consonant_1
        return consonant_1 + vowel_1

def increment(word):
    '''Adds signs to existing word.
    '''
    word += build_sign()
    return word

def main():
    '''This is mostly interface. Outer infinite loop continues
    execution until user chooses to exit. Inner loop increments
    word with signs until user chooses to stop, then offers to
    save word in word-list file.
    '''
    print(INTRO)
    input("\nPress any key to begin.")
    print()
    while True:
        word = ''
        flag = 'y'
        while flag == 'y':
            word = increment(word)
            print("The word is '{}'.".format(word))
            flag = input("Increment? ('y' or anything else to \
stop incrementing) ")
        flag_2 = input("Save word? ('y' or anything else to \
skip saving word) ")
        if flag_2 == 'y':
            with open(FILENAME, 'a') as handle:
                handle.write(word + '\n')
        flag_3 = input("Quit? ('y' or anything else to keep \
going with another word) ")
        if flag_3 == 'y':
            sys.exit(0)

if __name__=='__main__':
    main()