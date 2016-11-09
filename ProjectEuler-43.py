'''The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.'''


import itertools


pandigital_winners = []
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
X = itertools.permutations(L)
#X = [(1, 4, 0, 6, 3, 5, 7, 2, 8, 9)]
for n in X:
    while True:
        if not ((n[1] * 100) + (n[2] * 10) + n[3]) % 2 == 0:
            break
        if not ((n[2] * 100) + (n[3] * 10) + n[4]) % 3 == 0:
            break
        if not ((n[3] * 100) + (n[4] * 10) + n[5]) % 5 == 0:
            break
        if not ((n[4] * 100) + (n[5] * 10) + n[6]) % 7 == 0:
            break
        if not ((n[5] * 100) + (n[6] * 10) + n[7]) % 11 == 0:
            break
        if not ((n[6] * 100) + (n[7] * 10) + n[8]) % 13 == 0:
            break
        if not ((n[7] * 100) + (n[8] * 10) + n[9]) % 17 == 0:
            break

        # You made it this far, add it to the winner list
        pandigital_winners.append(n)
        break

print(pandigital_winners)

# ANSWER 16695334890
