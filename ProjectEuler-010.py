'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math


counter = 3
primes = [2]


while counter <= 1000:
    if counter % 100000 == 0:
        print(counter)
    for number in range(2, (int(math.ceil(math.sqrt(counter)))) + 1):
        top_of_range = (int(math.ceil(math.sqrt(counter))) + 1)
        if (counter % number) == 0:
            counter += 1
            break
        if (number + 1) == top_of_range:
            primes.append(counter)
            counter += 1

print(len(primes))
print(sum(primes))
