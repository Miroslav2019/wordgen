#Configuration file for the application. Values can be changed
#by the user as wished.
#
#The default character configuration for building signs is:
#
#    VOWELS - the five standard English-language vowels
#    CONS_1 - the five fixed-duration non-sibiliant consonants
#             that include an unextendable stop in
#             pronunciation (e.g. "b"/"buh")
#    CONS_2 - the three sibiliant consonants that can be
#             variable-duration sounds (e.g."ess" or "sssss")
#    CONS_3 - the five variable-duration consonants that can
#             be voicebox-enunciated voyelically (e.g. "ell"
#             or "lllll")
#    CONS_4 - the five uncertain-pronunciation consonants
#             (e.g. "x" and "j")

VOWELS = 'aeiou'
CONS_1 = 'bdgkpt'
CONS_2 = 'fhs'
CONS_3 = 'lmnrvz'
CONS_4 = 'cjqwx'

#The thresholds are set as follows:
#
#    CONS_1: over threshold of over threshold
#    CONS_2: under threshold of under threshold
#    CONS_3: over threshold of under threshold
#    CONS_4: under threshold of under threshold
#
#    V1-C1-V2 (e.g. "eka") - over of over
#    C1-V1-C2 (e.g. "keg") - under of over
#    V2-C1    (e.g. "ak")  - over of under
#    C2-V1    (e.g. "ge")  - under of under

THRESHOLD = 0.39

#The filename under which to save the list of words:

FILENAME = 'wordlist.txt'

#The credits text--NOT TO BE CHANGED:

CREDITS = '''
Ajalle's Wordlist Generator v0.1
(c) 2018 by Ajalle Perfej
'''

#The introductory blurb:

INTRO = '''
This Python 3 script generates random words. The words are built
one sign (syllable) at a time, and you choose when to stop adding
signs. You can discard any word or save it to a words list file
on disk.

To configure the script open 'config.py' in a text editor.
'''

#These are for the input jail idiot-proofing:

YESNO = '(y/n)'
OOPS = 'Must be "y" or "n".'

#These are assorted strings:

QUIT = "Quit program?"

