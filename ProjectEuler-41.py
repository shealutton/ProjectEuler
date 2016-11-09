'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?'''

#123,456,789
#987,654,321 would be the upper bound of pandigital anything, it uses all digits 1-9.

#1 find all primes 2-987,654,321 using the sieve of Erath

potential_prime_dict = {}
prime_dict = {2:None, 3:None, 5:None}
#for number in range(3, 987654322, 2):  # Populate the dict with every number 1 - X
for number in range(3, 1000000, 2):  # Populate the dict with every number 1 - X
    if not number % 3 == 0 and not number % 5 == 0:
        potential_prime_dict[number] = None

print(len(potential_prime_dict))

print("Starting prime calculation")
while potential_prime_dict:
    smallest = min(potential_prime_dict)
    prime_dict[smallest] = 0
    delete_list = []
    for key in potential_prime_dict:
        if key % smallest == 0:
            delete_list.append(key)

    for item in delete_list:
        potential_prime_dict.__delitem__(item)

print(len(prime_dict))
outfile = open('first-100mm-primes.txt', 'w')
for key in sorted(prime_dict.keys()):
    string = str(key) + '\n'
    outfile.write(string)

outfile.flush()
outfile.close()
