'''Shea's prime generator'''


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


x = prime_generator(100)
for prime in x:
    print(prime)
