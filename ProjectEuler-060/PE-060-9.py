'''The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''

import math


def prime_generator(limit):
    factors = [0] * limit
    for num in range(2, limit):
        if factors[num] == 0:
            # Then num must be prime
            multiple = num
            while multiple < limit:
                factors[multiple] += 1
                multiple += num

            if num == 2:
                pass
            else:
                yield num


def is_prime(n):
    for number in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if (n % number) == 0:
            return False
    return True


def is_prime2(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


def test(item):  # a = tuple or list
    if is_prime(int('{}{}'.format(item[0], item[1]))):
        if is_prime(int('{}{}'.format(item[1], item[0]))):
            return True
    return False


p = set()
for prime in prime_generator(20000):
    p.add(prime)

chain = []
sp = sorted(p)
for p1 in sp:
    for p2 in sp:
        if p2 > p1:
            if test((p1, p2)):
                chain.append(p1)
                chain.append(p2)
                for p3 in sp:
                    if p3 > p2:
                        if test((p3, p2)) and test((p3, p1)):
                            chain.append(p3)
                            for p4 in sp:
                                if p4 > p3:
                                    if test((p4, p3)) and test((p4, p2)) and test((p4, p1)):
                                        chain.append(p4)
                                        for p5 in sp:
                                            if p5 > p4:
                                                if test((p5, p4)) and test((p5, p3)) and test((p5, p2)) and test((p5, p1)):
                                                    chain.append(p5)
                                                    print('Winner', chain, sum(chain))
                                        chain.pop(-1)
                            chain.pop(-1)
                chain = []
