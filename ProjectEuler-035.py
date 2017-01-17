'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''


import math


def get_primes(maximum):
    counter = 3
    primes = {1: 0, 2: 0}
    while counter <= maximum:
        if counter % 100000 == 0:
            print(counter)
        for number in range(2, (int(math.ceil(math.sqrt(counter)))) + 1):
            top_of_range = (int(math.ceil(math.sqrt(counter))) + 1)
            if (counter % number) == 0:
                counter += 1
                break
            if (number + 1) == top_of_range:
                primes[counter] = 0
                counter += 1

    return primes


set_of_circular_primes = set()
list_of_primes = get_primes(1000000)

for item in list_of_primes:
    string = str(item)
    # Form the list of digits to iterate over
    list_of_digits = []
    for digit in string:
        list_of_digits.append(int(digit))

    iteration_set = set()
    counter = 0
    while counter < len(list_of_digits):
        X = list_of_digits.pop()
        list_of_digits.insert(0, X)
        iter_string = ''
        for digit in list_of_digits:
            iter_string = '{}{}'.format(iter_string, digit)
        iteration_set.add(int(iter_string))
        counter += 1

    circular = True
    for potential_circular in iteration_set:
        if potential_circular not in list_of_primes:
            circular = False
            break

    if circular:
        set_of_circular_primes.add(item)

print(len(set_of_circular_primes) -1, sorted(set_of_circular_primes))
