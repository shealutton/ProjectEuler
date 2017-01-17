'''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2
to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''


def validate_pattern(string, first_position, second_position):
    # For a pair of characters that match, check the rest of the string agains that pattern to verify they still match
    length = second_position - first_position  # How long is the repeating section to validate?
    # To simplify string matching, take a substring that trims off non-repeating sections at the front.
    substring = string[first_position:-1]
    for position in range(0, len(substring)):
        remainder = position % length
        if substring[remainder] == substring[position]:
            pass
        else:
            return 0

    return length


def check_for_patterns(string):
    # From the start of a string, take a char/digit in the first position and search the rest of the string for matches.
    # If a string has repeating patterns, that digit will be repeated someplace. Find all matches, then validate each.
    string = str(string)
    start_positon = 0
    while start_positon <= len(string):
        counter = start_positon + 1
        while counter < len(string) - 2:
            if string[start_positon] == string[counter]:
                #print('TEST', string[0:40], start_positon, counter, string[start_positon], string[(counter-3):(counter+3)], len(string))
                result = validate_pattern(string, start_positon, counter)
                if result > 0:
                    return result
                counter += 1
            else:
                counter += 1
        start_positon += 1

    return 0


def long_division(divisor, dividend):
    quotient = '0'
    while True:
        if divisor > dividend and quotient == '0':
            # Add 10 to dividend and add extra decimal place to quotient
            dividend *= 10
            quotient = '{0}{1}'.format(quotient, '.')
        elif divisor > dividend:
                # Add 10 to dividend and add extra decimal place to quotient
                dividend *= 10
                quotient = '{0}{1}'.format(quotient, '0')
        elif (dividend % divisor) == 0:
            quotient = '{0}{1}'.format(quotient, (dividend // divisor))
            return quotient
        else:
            quotient = '{0}{1}'.format(quotient, (dividend // divisor))
            dividend %= divisor
            dividend *= 10

        if len(quotient) >= 5000:
            return quotient


counter = 2
while counter < 1000:
    decimal = long_division(counter, 1)
    decimal_string = decimal[2:-1]
    repeating_length = check_for_patterns(decimal_string)
    print(repeating_length, counter, decimal)
    counter += 1

# ANSWER = 983. Notice that many prime numbers (n) have a repeating cycle of (n - 1). 983 has a cycle of 982.