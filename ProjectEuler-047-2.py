'''The first two consecutive numbers to have two distinct prime factors are:
14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
numbers? # Note that if a number is prime, it can't have 4 distinct factors. You are looking for 4 consecutive
non-primes'''


limit = 1000000
factors = [0] * limit
count = 0
for num in range(2, limit):
    if factors[num] == 0:
        # Then num must be prime
        multiple = num
        count = 0
        while multiple < limit:
            factors[multiple] += 1
            multiple += num
    elif factors[num] == 4:  # Looking for 4 consecutive numbers with 4 factors. This is one. Count += 1
        count += 1
        if count == 4:
            print(num-3)
            break
    else:
        count = 0
