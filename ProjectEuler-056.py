'''A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?'''


def string_value(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


max = 0
for a in range(1, 100):
    for b in range(1, 100):
        test = string_value(a ** b)
        if test > max:
            max = test
            winner = (a, b)

print(winner, max)


