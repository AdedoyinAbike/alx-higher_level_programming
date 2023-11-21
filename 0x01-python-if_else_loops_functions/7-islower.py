#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'
if islower(c):
    print('{} is lower'.format(c))
else:
    print('upper')
c= 'a'
islower(c)
