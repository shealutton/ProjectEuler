'''The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''

import itertools


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


def four_test(a, b, c, d):
    x = itertools.permutations([a, b, c, d], 2)
    for item in x:
        if int('{}{}'.format(item[0], item[1])) in p:
            pass
        else:
            return False
    return True


def five_test(a, b, c, d, e):
    x = itertools.permutations([a, b, c, d, e], 2)
    for item in x:
        if int('{}{}'.format(item[0], item[1])) in p:
            pass
        else:
            return False
    return True


p = set()
for prime in prime_generator(20000):
    p.add(prime)

prime_combinations = itertools.combinations(p, 5)

for i in prime_combinations:
    print(i)
    if five_test(i[0], i[1], i[2], i[3], i[4]):
        print(sum([i[0], i[1], i[2], i[3], i[4]]))
        break
