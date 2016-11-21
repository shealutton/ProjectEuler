'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import sys


for a_num in range(1,1000):
    for b_num in range(1, 1000):
        for c_num in range(1, 1000):
            a_sq = a_num ** 2
            b_sq = b_num ** 2
            c_sq = c_num ** 2

            if (a_sq + b_sq) == c_sq:
                if (a_num + b_num + c_num) == 1000:
                    print(a_num, b_num, c_num)
                    print(a_num * b_num * c_num)

                    sys.exit(0)