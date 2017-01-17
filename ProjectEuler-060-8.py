'''The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.'''


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


def test(item, unused):  # a = tuple or list
    if int('{}{}'.format(item[0], item[1])) not in primes:
        return False
    if int('{}{}'.format(item[1], item[0])) not in primes:
        return False
    return True


p = set()
primes = set()
for prime in prime_generator(84000000):
    primes.add(prime)
    if prime < 10000:
        p.add(prime)

chain = []
sp = sorted(p)
for p1 in sp:
    for p2 in sp:
        if p2 > p1:
            if test((p1, p2), 2):
                chain.append(p1)
                chain.append(p2)
                for p3 in sp:
                    if p3 > p2:
                        if test((p3, p2), 2) and test((p3, p1), 2):
                            chain.append(p3)
                            for p4 in sp:
                                if p4 > p3:
                                    if test((p4, p3), 2) and test((p4, p2), 2) and test((p4, p1), 2):
                                        chain.append(p4)
                                        for p5 in sp:
                                            if p5 > p4:
                                                if test((p5, p4), 2) and test((p5, p3), 2) and test((p5, p2), 2) and test((p5, p1), 2):
                                                    chain.append(p5)
                                                    print('Winner', chain, sum(chain))
                                        chain.pop(-1)  # There were no winners with the 4th level in the chain, remove
                            chain.pop(-1)  # There were no winners from the 3rd level
                chain = []  # No winners in the first or second levels.
