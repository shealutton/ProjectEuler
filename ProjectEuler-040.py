'''An irrational decimal fraction is created by concatenating the positive integers, 1, 2, 3, ... 11, 12 ... :

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10,000 × d100,000 × d1,000,000'''

counter = 1
string = '.'
while len(string) < 1000002:
    string = '{0}{1}'.format(string, counter)
    counter += 1

print(int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) *
      int(string[100000]) * int(string[1000000]))

