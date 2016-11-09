'''A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

import sys


counter = 998001
palindromes = []

while 10000 <= counter <= 998001:
    string = str(counter)
    if string == string[::-1]:
        palindromes.append(counter)
    counter -= 1

print(palindromes)


for item in palindromes:
    divisor = 999
    while divisor >= 100:
        if (item % divisor) == 0:
            result = str(int(item / divisor))
            if len(result) == 3:
                print(result, item, divisor)
                sys.exit(0)
        divisor -= 1
