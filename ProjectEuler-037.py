#!/usr/bin/python
# USE PYTHON 2.7!

'''The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.'''

import sys
import math

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


def in_list(question):
    if question in prime_list:
        return True
    else:
        return False


prime_list = rwh_primes2(1000000)
print('Starting truncation')
winning_list = []
for prime in prime_list:
    winner = True
    denominator = 10
    for iteration in range(1, len(str(prime))):
        left = prime / denominator
        right = prime % denominator
        if not in_list(left) or not in_list(right):
            winner = False
            break
        denominator *= 10

    if winner:
        winning_list.append(prime)

    if len(winning_list) >= 15:
        print(sum(winning_list) - 17)
        break

print(len(winning_list), winning_list)