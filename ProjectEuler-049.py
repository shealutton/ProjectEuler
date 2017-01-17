'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?'''
import sys


def prime_generator(limit):
    factors = [0] * limit
    for num in range(2, limit):
        if factors[num] == 0:
            # Then num must be prime
            multiple = num
            while multiple < limit:
                factors[multiple] += 1
                multiple += num
            yield num


def permutations(a, b, c):
    if a == 1487 and b == 4817 and c == 8147:
        pass
    elif sorted(str(a)) ==  sorted(str(b)) and sorted(str(c)) ==  sorted(str(b)):
        print(a, b, c, '{0}{1}{2}'.format(a, b, c))
        sys.exit(0)


x = prime_generator(10000)
p = {}
for prime in x:
    if prime > 1000:
        p[prime] = None

for outer in p:
    for inner in p:
        if inner == outer:
            pass
        else:
            delta = outer - inner
            if delta > 0:
                if outer + delta in p:
                    permutations(inner, outer, outer + delta)

