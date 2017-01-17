'''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''

i = 1
while True:
    if sorted(str(i)) == sorted(str(i*2)):
        if sorted(str(i)) == sorted(str(i * 3)):
            if sorted(str(i)) == sorted(str(i * 4)):
                if sorted(str(i)) == sorted(str(i * 5)):
                    if sorted(str(i)) == sorted(str(i * 6)):
                        print(i, i*2, i*3, i*4, i*5, i*6)
                        break
    i += 1
