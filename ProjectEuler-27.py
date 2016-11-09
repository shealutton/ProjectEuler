'''Euler discovered the remarkable quadratic formula n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when
n=40, 40^2 + 40 + 41 is divisible by 41, and certainly when n=41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values
0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
primes for consecutive values of n, starting with n=0.'''


def open_primes():
    prime_dict = {}
    prime_file = open('million_primes.txt', 'r')
    line = prime_file.readline()
    items = line.split(',')
    for item in items:
        prime_dict[int(item)] = 0
    return prime_dict


primes = open_primes()
current_winner = False
max_length = 0

for a in range(0, 1000):
    for b in range(0, 1001):
        list_of_primes_pp = []
        list_of_primes_pn = []
        list_of_primes_np = []
        list_of_primes_nn = []
        n = 0
        PP = True
        PN = True
        NP = True
        NN = True
        while PP and PN and NP and NN:
            if PP:
                answer_pp = (n ** 2) + (a * n) + b
                if answer_pp in primes:
                    list_of_primes_pp.append(answer_pp)
                else:
                    if len(list_of_primes_pp) >= max_length:
                        #print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes_pp))
                        max_length = len(list_of_primes_pp)
                        current_winner = (a, b)
                    PP = False
            if PN:
                answer_pn = (n ** 2) + (a * n) + (-b)
                if answer_pn in primes:
                    list_of_primes_pn.append(answer_pn)
                else:
                    if len(list_of_primes_pn) >= max_length:
                        #print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes_pn))
                        max_length = len(list_of_primes_pn)
                        current_winner = (a, -b)
                    PN = False
            if NP:
                answer_np = (n ** 2) + (-a * n) + b
                if answer_np in primes:
                    list_of_primes_pn.append(answer_np)
                else:
                    if len(list_of_primes_np) >= max_length:
                        #print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes_np))
                        max_length = len(list_of_primes_np)
                        current_winner = (-a, b)
                    NP = False
            if NN:
                answer_nn = (n ** 2) + (-a * n) + (-b)
                if answer_nn in primes:
                    list_of_primes_pn.append(answer_nn)
                else:
                    if len(list_of_primes_nn) >= max_length:
                        #print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes_nn))
                        max_length = len(list_of_primes_nn)
                        current_winner = (-a, -b)
                    NN = False
            print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes_pp), len(list_of_primes_pn),
                  len(list_of_primes_np), len(list_of_primes_nn))
            n += 1

print(current_winner, max_length, 'Product of AB:', (current_winner[0] * current_winner[1]))