'''There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5^C3 (the 5 is up left, the 3 is below right) = 10.

In general, nCr = n! / ( r!(n−r)! ) ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1,144,066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''


from scipy.special import factorial


counter = 0
for n in range(23, 101):
    for d in range(2,n-1):
        if factorial(n) // (factorial(d) * factorial(n - d)) >= 1000000:
            counter += 1

print('Brute force:', counter)
