#Ajalle's Wordlist Generator
#(c) 2018 by Ajalle Perfej
#
#Main file of script.
#For functions see file 'functions.py'
#To configure see file 'config.py'

import sys
import functions as fun
from config import CREDITS, INTRO, YESNO, OOPS, QUIT

def main():
    print(CREDITS)
    print(INTRO)
    while True:
        word = fun.build_word()
        if word:
            save_word()
        while True:
            flag = input("{} {}".format(QUIT, YESNO))
            if flag == 'y':
                sys.exit(0)
            elif flag != 'n':
                print(OOPS)