#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last = number % 10
if number < 0:
    last = 10 + last * (-1)
if last == 0:
    line = ('Last digit of ' + str(number) +
            ' is ' + str(last) + ' and is zero')
else:
    if last > 5:
        line = ('Last digit of ' + str(number) +
                ' is ' + str(last) + ' and is greater' +
                ' than 6 and not 0')
    elif last < 5:
        line = ('Last digit of ' + str(number) +
                ' is ' + str(last) + ' and is less' +
                ' than 6 and not 0')
print(line)
