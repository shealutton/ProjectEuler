'''
Longest Collatz Sequence

n becomes n/2 (if n is even)
n becomes 3n + 1 (if n is odd)

Starting at 13 produces: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

Which starting number, under 1,000,000 produces the longest chain?
'''

winning_chain = []
winning_number = 0

for number in range(1, 1000000):
    chain = [number]
    working_number = number
    while not working_number == 1:
        if (working_number % 2) == 0:
            working_number = int(working_number / 2)
            chain.append(working_number)
#            print(number, working_number, chain)
        else:
            working_number = (3 * working_number) + 1
            chain.append(working_number)
#            print(number, working_number, chain)

    if len(chain) > len(winning_chain):
        winning_chain = chain
        winning_number = number
        print(winning_number, len(winning_chain), winning_chain)
