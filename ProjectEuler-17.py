'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage.'''


def ones(digit):
    if digit == 1:
        return 3  # one
    elif digit == 2:
        return 3  # two
    elif digit == 3:
        return 5  # three
    elif digit == 4:
        return 4  # four
    elif digit == 5:
        return 4  # five
    elif digit == 6:
        return 3  # six
    elif digit == 7:
        return 5  # seven
    elif digit == 8:
        return 5  # eight
    elif digit == 9:
        return 4  # nine


def tens(digit):
    if digit == 2:
        return 6  # twenty
    elif digit == 3:
        return 6  # thirty
    elif digit == 4:
        return 5  # forty
    elif digit == 5:
        return 5  # fifty
    elif digit == 6:
        return 5  # sixty
    elif digit == 7:
        return 7  # seventy
    elif digit == 8:
        return 6  # eighty
    elif digit == 9:
        return 6  # ninety


def ten_handler(digits):
    if 0 <= digits < 10:
        return ones(int(digits))
    elif 10 <= digits < 20:  # if number is 10 through 19, handle the teens
        if digits == 10:
            return 3  # eleven
        if digits == 11:
            return 6  # eleven
        elif digits == 12:
            return 6  # twelve
        elif digits == 13:
            return 8  # three
        elif digits == 14:
            return 8  # four
        elif digits == 15:
            return 7  # five
        elif digits == 16:
            return 7  # six
        elif digits == 17:
            return 9  # seven
        elif digits == 18:
            return 8  # eight
        elif digits == 19:
            return 8  # nine
    else:
        tens_column = int(str(digits)[0])
        ones_column = int(str(digits)[1])
        T = tens(tens_column)
        if ones_column == 0:
            O = 0
        else:
            O = ones(int(ones_column))

        total = int(T) + int(O)
        return total


def hundreds(digits):
    if 100 <= digits < 200:
        hun_column = 13
    elif 200 <= digits < 300:
        hun_column = 13
    elif 300 <= digits < 400:
        hun_column = 15
    elif 400 <= digits < 500:
        hun_column = 14
    elif 500 <= digits < 600:
        hun_column = 14
    elif 600 <= digits < 700:
        hun_column = 13
    elif 700 <= digits < 800:
        hun_column = 15
    elif 800 <= digits < 900:
        hun_column = 15
    elif 900 <= digits < 1000:
        hun_column = 14

    if (digits % 100) == 0:  # if the number is divisible by 100 (ie, 100, 200, 300, etc)
        tens_subtotal = -3  # remove 3 chars to negate the 'and' from 'one hundred and'
    else:
        tens_column = int(str(digits)[-2:])
        tens_subtotal = ten_handler(tens_column)

    total = tens_subtotal + hun_column
    return total


letter_total = 0
for number in range(1, 1001):
    if 0 < number < 10:
        letter_total += ones(number)
    elif 10 <= number < 100:
        letter_total += ten_handler(number)
    elif 100 <= number < 1000:
        letter_total += hundreds(number)
    elif number == 1000:
        letter_total += 11  # onethousand

print(letter_total)

