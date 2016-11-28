'''Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?'''


def is_pandigital(pan_string):
    sorted_string = sorted(str(pan_string))
    length = len(sorted_string) + 1
    pandigital = True
    for digit in range(1, length):
        if not digit == int(sorted_string[digit - 1]):
            pandigital = False
            break
    if pandigital:
        return True


winner = 0
for integer in range(2, 9999):
    string = ''
    for second_int in range(1,9):
        string = '{}{}'.format(string, integer * second_int)
        if len(string) == 9:
            if is_pandigital(string):
                if int(string) > winner:
                    winner = int(string)
        elif len(string) > 9:
            break

print(winner)