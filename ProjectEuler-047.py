'''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
numbers?'''

# Note that if a number is prime, it can't have 4 distinct factors. You are looking for 4 consecutive non-primes

from __future__ import print_function
import itertools
import sys


def factors(number):
    factors_set = set()
    bottom = 2
    top = number

    while bottom < top:
        if (number % bottom) == 0:
            top = int(number / bottom)
            factors_set.add(bottom)
            factors_set.add(top)
        bottom += 1

    return factors_set


def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0: n, 1: n-1, 2: n+4, 3: n+3, 4: n+2, 5: n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


def get_sets(n):
    initial_list = sorted(factors(n))
    F = []
    for item in initial_list:
        if item in P:
            F.append(item)
            if item**2 < n / 2:
                F.append(item**2)

    if len(F) < 4:
        return 0

    to_do = itertools.combinations(F, 4)
    for item in to_do:
        if item[0] * item[1] * item[2] * item[3] == n:
            return item

    return 0


winner_dict = {}
P = rwh_primes2(140000)
counter = 0
for number in range(10000, 140000):
    if number % 5000 == 0:
        print(number)
    if number in P:
        pass  # Skip all prime numbers, they can't have n distinct factors by definition
    else:
        returned_set = get_sets(number)
        if not returned_set == 0:
            winner_dict[number] = returned_set

            if number - 1 in winner_dict:
                if number - 2 in winner_dict:
                    if number - 3 in winner_dict:
                        print(number - 3, winner_dict[number], winner_dict[number - 1], winner_dict[number - 2],
                              winner_dict[number - 3])
                        sys.exit(0)