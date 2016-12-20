'''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

# 1. Find all primes
# 2. Find all odd non-primes
# 3. For each prime smaller than the #, add all squares until > #, pass


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


P = rwh_primes2(10000)
twice_squares = {}
for number in range(1, 1001):
    twice_squares[(2 * (number ** 2))] = number

for number in range(9, 10000, 2):
    solved = False
    if number not in P:  # Only check odd composite (non-prime) integers
        for ts in twice_squares:
            for prime in P:
                if prime + ts == number:
                    solved = True
                    print(number, prime, ts, 'WIN')
                    break
        if not solved:
            print("FAILED!", number)
            sys.exit(0)


