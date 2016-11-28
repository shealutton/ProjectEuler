'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.'''

counter = 1
answer = 1
for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        real_answer = numerator / denominator
        numerator_ones = numerator % 10
        numerator_tens = numerator // 10
        denominator_ones = denominator % 10
        denominator_tens = denominator // 10

        try:
            if numerator_ones > 0:
                if numerator_ones == denominator_tens:
                    if numerator_tens / denominator_ones == real_answer:
                        print(numerator, denominator, real_answer)
                        answer *= real_answer
        except ZeroDivisionError:
            pass

print(round(answer,4))
# the value of the denominator of .01 == 100. 100 is the answer.