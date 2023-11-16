#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'
char_input = input('enter a c: ')
if islower(char_input):
    print(f'{char_input} is lower')
else:
    print(f'{char_input} is upper')
