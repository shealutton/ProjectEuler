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
        list_of_primes = []
        n = 0
        while True:
            #answer = (n ** 2) + (a * n) + b
            answer = (n ** 2) + (-a * n) + b
            #answer = (n ** 2) + (a * n) + -b
            #answer = (n ** 2) + (-a * n) + -b
            if answer in primes:
                list_of_primes.append(answer)
                n += 1
            else:
                if len(list_of_primes) >= max_length:
                    print('A', a, 'B', b, 'N', n, 'Length', len(list_of_primes))
                    max_length = len(list_of_primes)
                    current_winner = (-a, b)
                break

print(current_winner, max_length, 'Product of AB:', (current_winner[0] * current_winner[1]))