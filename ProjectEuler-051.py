'''By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43,
53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.'''

# Could I use a mask to better effect? - Shea
# n=75703, mask=[0, 1, 1, 1, 1], counter=1
# out=71111
# n=75703, mask=[0, 1, 1, 1, 1], counter=2
# out=72222
# ...
# n=75703, mask=[1, 0, 0, 1, 1], counter=5
# out=55755


import itertools
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


def generate_masks():
    n_to_check_for_prime = set()
    x = itertools.permutations('100000', 6)
    for item in x:
        n_to_check_for_prime.add(item)
    x = itertools.permutations('110000', 6)
    for item in x:
        n_to_check_for_prime.add(item)
    x = itertools.permutations('111000', 6)
    for item in x:
        n_to_check_for_prime.add(item)
    x = itertools.permutations('111100', 6)
    for item in x:
        n_to_check_for_prime.add(item)
    x = itertools.permutations('111110', 6)
    for item in x:
        n_to_check_for_prime.add(item)

    return n_to_check_for_prime


x = prime_generator(1000000)
p = set()
for prime in x:
    if prime > 100000:
        p.add(prime)

masks = generate_masks()
for number in sorted(p):
    number = str(number)
    for mask in masks:  # Get one mask
        list_of_family_members = []
        for counter in range(0, 10):  # Substitute in values 0-9
            new_integer = []  # holding place for the new integer
            position = 0
            for mask_digit in mask:
                if mask_digit == '0':
                    new_integer.append(number[position])
                else:
                    new_integer.append(str(counter))
                position += 1

            list_of_family_members.append(int(''.join(new_integer)))

        prime_count = 0
        for num in list_of_family_members:
            if num in p:
                prime_count += 1
            if prime_count == 8:
                for item in list_of_family_members:
                    if item in p:
                        print(item)
                sys.exit(0)
