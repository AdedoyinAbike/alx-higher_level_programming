#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'
print('a is {}'.format('lower' if islower('a') else 'upper'))
print('H is {}'.format('lower' if islower('H') else 'upper'))
islower(c)
