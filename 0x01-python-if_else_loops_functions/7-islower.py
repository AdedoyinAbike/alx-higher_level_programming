#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'
c = 'a'
if islower(c):
    print('{} is lower'.format(c))
else:
    print('upper')
islower(c)
