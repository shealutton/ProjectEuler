'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''


def factors(number):
    factors_set = set()
    bottom = 1
    top = number

    while bottom < top:
        if (number % bottom) == 0:
            top = int(number / bottom)
            factors_set.add(bottom)
            factors_set.add(top)
        bottom += 1

    answer = sum(factors_set) - number
    return answer


amicable_numbers = []
list_of_numbers = []
for num in range(1, 10000):
    list_of_numbers.append(num)

while list_of_numbers:
    num = list_of_numbers.pop()
    factor_sum_first = factors(num)
    if factor_sum_first in list_of_numbers:
        factor_sum_second = factors(factor_sum_first)
    if factor_sum_second == num:
        #print(num, factor_sum_first, "\n", factor_sum_first, factor_sum_second)
        amicable_numbers.append(num)
        amicable_numbers.append(factor_sum_first)

print(sum(amicable_numbers))