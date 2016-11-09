'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''

counter = 3
primes = [2]

goal = 10001

while len(primes) <= (goal - 1):
    #print(counter)
    for number in range(2, counter):
        if (counter % number) == 0:
            counter += 1
            break
        if (number + 1) == counter:
            primes.append(counter)
            counter += 1

print(primes, primes[-1])
