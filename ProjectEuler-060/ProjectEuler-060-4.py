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


def test(a, goal):  # a = tuple or list
    x = itertools.permutations(a, goal)
    for item in x:
        if int('{}{}'.format(item[0], item[1])) not in p:
            return False

    return True


def prime_combinations(primes, goal):
    for item in itertools.combinations(sorted(primes), goal):
        yield item


p = set()
for prime in prime_generator(200000000):
    p.add(prime)
print('Finished Prime Generation')

pair_4 = set()
for prime in p:
    i = (673, prime)
    if test(i, 2):
        pair_4.add(i[0])
        pair_4.add(i[1])
print(len(pair_4), pair_4)

pair_3 = set()
for prime in pair_4:
    i = (109, prime)
    if test(i, 2):
        pair_3.add(i[0])
        pair_3.add(i[1])
print(len(pair_3), pair_3)

pair_2 = set()
for prime in pair_3:
    i = (7, prime)
    if test(i, 2):
        pair_2.add(i[0])
        pair_2.add(i[1])
print(len(pair_2), pair_2)

pair_1 = set()
for prime in pair_2:
    i = (3, prime)
    if test(i, 2):
        pair_1.add(i[0])
        pair_1.add(i[1])
print(len(pair_1), pair_1)