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

            if num == 2:
                pass
            else:
                yield num


def test(a, goal):  # a = tuple or list
    x = itertools.permutations(a, goal)
    for item in x:
        if int('{}{}'.format(item[0], item[1])) not in primes:
            return False

    return True


def prime_combinations(primes, goal):
    for item in itertools.combinations(sorted(primes), goal):
        yield item


p = set()
primes = set()
for prime in prime_generator(68000000):
    primes.add(prime)
    if prime < 30000:
        p.add(prime)


checked_d = {}
pairs_d = {}
for p1 in p:
    # Create the checked entry so I don't have to check every time
    if p1 not in checked_d:
        checked_d[p1] = set()

    # Now iterate over the list again to get the whole second set
    for p2 in p:
        if p2 not in checked_d:
            checked_d[p2] = set()

        if p2 not in checked_d[p1]:
            # If not in one, neither have been checked. Add to both sets.
            checked_d[p1].add(p2)
            checked_d[p2].add(p1)

            if test((p1, p2), 2):
                if p1 not in pairs_d:
                    pairs_d[p1] = {p2}
                else:
                    pairs_d[p1].add(p2)

                if p2 not in pairs_d:
                    pairs_d[p2] = {p1}
                else:
                    pairs_d[p2].add(p1)

con_d = {}  # dict for contending
while pairs_d:
    # Start pulling things out of the pairs_d, if they have at least 4 other matches, add them to final candidates pool
    x = pairs_d.popitem()
    if len(x[1]) >= 4:  # If they don't have at least 4 others they match with, they can't be one of the finalists
        con_d[x[0]] = x[1]

#for item in con_d:
#    perms = itertools.combinations(con_d[item], 4)

perms = itertools.combinations(pairs_d[8389], 4)
for p1, p2, p3, p4 in perms:
    if p1 in con_d and p2 in con_d and p3 in con_d and p4 in con_d:  # Check that all p's are left in con_d. 
        if p2 in con_d[p1] and p3 in con_d[p1] and p4 in con_d[p1]:
            if p1 in con_d[p2] and p3 in con_d[p2] and p4 in con_d[p2]:
                if p1 in con_d[p3] and p2 in con_d[p3] and p4 in con_d[p3]:
                    if p1 in con_d[p4] and p2 in con_d[p4] and p3 in con_d[p4]:
                        print('Winner', p1 + p2 + p3 + p4, item, p1, p2, p3, p4)
                        break

