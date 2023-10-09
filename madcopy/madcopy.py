import re
import sys
import os
if __name__ == "__main__":
    s='''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
    unaffected by these events.'''
    wordregex=re.compile(r'ADJECTIVE|VERB|NOUN')
    bigregex=re.compile(r'[A-Z]+')
    word=wordregex.findall(s)
    print(word)
    for solo in word:
            print(solo)
            your_input=str(input(''))
            one=re.compile(solo)
            s=one.sub(your_input,s)
            print(s)
    print(s)
