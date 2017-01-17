'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?'''

import collections


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


x = prime_generator(1000000)
p = []
for prime in x:
    p.append(prime)

'''placeholder = 0
while placeholder < len(p):
    total = sum(p[placeholder:placeholder + 21])
    if total in p:
        print('Winner 1', p[placeholder:placeholder + 21], total)
        break
    placeholder += 1
sys.exit(0)
'''

# Create a copy of P list
# pop items off the right and sum until sum in p.
# Copy new list x = p[1:n], omitting the front item, repeat

winner = (0, 0)
length = len(p)
dq = collections.deque(p[0:546])
print(sum(dq))
for counter in range(length):
    while dq:
        if sum(dq) in p:  # If the sum of the new list is prime, then that is the max number of terms
            if len(dq) > winner[1]:
                winner = (sum(dq), len(dq), dq)
                break
            else:
                break
        else:
            junk = dq.pop()
    junk = dq.popleft()

print('Final', winner)