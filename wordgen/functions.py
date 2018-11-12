#This is the functions file
#For the main script see the file 'main.py'
#To configure see the file 'config.py'

import random as rnd
import config as kon

def choose_consonant_list():
    '''see config.py for how consonants are grouped.'''
    if rnd.random() > kon.THRESHOLD:
        if rnd.random() > kon.THRESHOLD:
            return kon.CONS_1
        return kon.CONS_2
    else:
        if rnd.random() > kon.THRESHOLD:
            return kon.CONS_3
        return kon.CONS_4

def choose_letters(consonant_list):
    '''based on choice in choose_consonant_list() and on
    VOWELS list in config.py
    '''
    consonant_1 = rnd.choice(consonant_list)
    consonant_2 = rnd.choice(consonant_list)
    vowel_1 = rnd.choice(kon.VOWELS)
    vowel_2 = rnd.choice(kon.VOWELS)
    return consonant_1, consonant_2, vowel_1, vowel_2

def build_sign(consonant_1, consonant_2, vowel_1, vowel_2):
    '''See file 'config.py' for constants and pattern
    '''
    if rnd.random() > kon.THRESHOLD:
        if rnd.random() > kon.THRESHOLD:
            return vowel_1 + consonant_1 + vowel_2
        return consonant_1 + vowel_1 + consonant_2
    else:
        if rnd.random() > kon.THRESHOLD:
            return vowel_2 + consonant_1
        return consonant_2 + vowel_1

def build_word():
    word = ''
    flag = 'y'
    consonant_list = choose_consonant_list()
    while flag == 'y':
        consonant_1, consonant_2, vowel_1, vowel_2 =\
        choose_letters(consonant_list)
        sign = build_sign(consonant_1, consonant_2,\
        vowel_1, vowel_2)
        word += sign
        while True:
            print("\nThe word so far is '{}'.".format(word))
            flag = input("Add more signs? {}".format(kon.YESNO))
            if flag == 'n':
                return word
            elif flag != 'y':
                print(kon.OOPS)
            else:
                break

def save_word(word):
    while True:
        flag = input("Save word '{}'? {}".format(word, kon.YESNO))
        if flag == 'y':
            with open (kon.FILENAME, 'a') as handle:
                handle.write(word + '\n')
                return
        elif flag == 'n':
            return
        print(kon.OOPS)