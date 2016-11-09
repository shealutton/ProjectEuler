'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''


number = 600851475143
remaining = number
counter = 2
factors_set = set()

while counter <= remaining:
    if (remaining % counter) == 0:
        remaining = (remaining / counter)
        factors_set.add(counter)
    else:
        counter += 1

print(sorted(factors_set))