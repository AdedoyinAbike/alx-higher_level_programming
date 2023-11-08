#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(f"{str[str.index('object-oriented programming')].strip()}")
print(str)
