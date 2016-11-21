'''The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)'''


def is_pal(number):
    string = str(number)
    if string == string[::-1]:
        return True
    else:
        return False


double_pal = []

for item in range(1, 1000001):
    if is_pal(item) and is_pal(format(item, 'b')):
        double_pal.append(item)

print(sum(double_pal), double_pal)