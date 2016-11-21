#!/usr/bin/python
# USE PYTHON 2.7!

'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?'''

#123,456,789
#987,654,321 would be the upper bound of pandigital anything, it uses all digits 1-9.

#1 find all primes 2-987,654,321 using the sieve of Erath

import sys


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


L = rwh_primes2(987654322)
#L = rwh_primes2(100000000)
#outfile = open('temp-primes.txt', 'w')
#for item in L:
#    string = str(item) + '\n'
#    outfile.write(string)#

#outfile.flush()
#outfile.close()

while True:
    prime = L.pop()
    string = sorted(str(prime))
    length = len(string) + 1
    pandigital = True
    for digit in range(1, length):
        #print(prime, digit, int(string[digit - 1]))
        if not digit == int(string[digit - 1]):
            pandigital = False
            break
    if pandigital:
        print(prime)
        sys.exit(0)




