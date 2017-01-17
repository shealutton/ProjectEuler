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
for prime in prime_generator(700000):
    p.add(prime)

p_subset = set()
for prime in p:
    if 2 < prime < 2000:
        p_subset.add(prime)

pair_set = set()
for i in prime_combinations(p_subset, 2):
    if test(i, 2):  # Find pairs of primes to then search out a group of 5
        pair_set.add(i[0])
        pair_set.add(i[1])

for i in prime_combinations(sorted(pair_set), 2):
    if test(i, 2):
        print(sum(i), i)
        break
