'''The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''



counter = 1
list_of_squares = []
list_of_numbers = []

while counter <= 100:
    list_of_squares.append(counter ** 2)
    list_of_numbers.append(counter)
    counter += 1

diff = (sum(list_of_numbers) ** 2) - sum(list_of_squares)
print(diff)