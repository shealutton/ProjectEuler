'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

import sys


num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counter = 9552209
found = False

while not found:
    #print(counter)
    for item in num_list:
        if (counter % item) == 0:
            if item == num_list[-1]:
                found = True
                print(counter)
                break
        else:
            counter += 1
            break