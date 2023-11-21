#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'


def islower():
    return 'a' <= c <= 'z'


print('a => {}'.format('lower' if islower('a') else 'upper'))


islower(c)
