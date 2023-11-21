#!/usr/bin/python3
def uppercase(str):
    result = ''
    for ch in str:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - ord('a') + ord('A'))
        else:
            result += ch
    print('{}'.format(result))
