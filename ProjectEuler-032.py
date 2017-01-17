'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
 the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.'''


import itertools


pandigital_set = set()
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = itertools.permutations(L)
for n in X:
    # x * yyyy = zzzz
    if n[0] * ((n[1] * 1000) + (n[2] * 100) + (n[3] * 10) + n[4]) == (n[5] * 1000) + (n[6] * 100) + (n[7] * 10) + n[8]:
        pandigital_set.add(n)
    # xx * yyy = zzzz
    if ((n[0] * 10) + n[1]) * ((n[2] * 100) + (n[3] * 10) + n[4]) == (n[5] * 1000) + (n[6] * 100) + (n[7] * 10) + n[8]:
        pandigital_set.add(n)
    # xxx * yy = zzzz
    if (((n[0] * 100) + (n[1] * 10) + n[2]) * ((n[3] * 10) + n[4]) == (n[5] * 1000) + (n[6] * 100) + (n[7] * 10) + n[8]):
        pandigital_set.add(n)
    # xxxx * y = zzzz
    if (((n[0] * 1000) + (n[1] * 100) + (n[2] * 10) + n[3]) * n[4]) == ((n[5] * 1000) + (n[6] * 100) + (n[7] * 10) + n[8]):
        pandigital_set.add(n)

new_set = set()
for i in pandigital_set:
    string = '{}{}{}{}'.format(i[5], i[6], i[7], i[8])
    new_set.add(int(string))

print(sum(new_set))