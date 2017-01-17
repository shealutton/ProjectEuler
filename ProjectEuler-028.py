'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

   21 22 23 24 25
   20  7  8  9 10
   19  6  1  2 11
   18  5  4  3 12
   17 16 15 14 13

43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49
x,    x,    x     x     x              x               x               x               x                 x                 x                 x                 x
ul    dl    ul    dl    ul             dl              ul              dl              ul                dl                ul                dl                ul
'''

place = 1
box_size = 1
increment_by = 2
diag_up_left = []
diag_down_left = []

diag_up_left.append(place)
while box_size < 1001:
    place += increment_by
    diag_down_left.append(place)
    place += increment_by
    diag_up_left.append(place)
    place += increment_by
    diag_down_left.append(place)
    place += increment_by
    diag_up_left.append(place)
    increment_by += 2
    box_size += 2

print(sum(diag_down_left) + sum(diag_up_left))