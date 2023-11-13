#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print('{}{}'.format(i,j) if i < j else '{}{}'.format(j,i), end=', ')
