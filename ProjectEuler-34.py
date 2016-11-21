'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''


def factorial(num):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total


result_list = []
for number in range(3, 50000):
    string = str(number)
    factorial_total = 0
    for digit in string:
        factorial_total += factorial(int(digit))

    if int(factorial_total) == number:
        result_list.append(number)

print(sum(result_list), result_list)
