'''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?'''

#1. determine triangle numbers up to n=10,000, store in dict, the largest t = 49,995,000
#2. build word to value calculator, quick lookup in the t_dict
#3. count triangle words


triangle_word_count = 0
triangle_dict = {}
letter_dict = {'"': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
               'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
               'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def word_value_calculator(passed_word):
    total = 0
    for letter in passed_word:
        total += letter_dict[letter]
    return total


for number in range(1, 10000):
    t_number = int((.5 * number) * (number + 1))
    triangle_dict[t_number] = None


words_file = open('p042_words.txt', 'r')
lines = words_file.readlines()
for line in lines:
    words = line.split(',')
    for word in words:
        value = word_value_calculator(word.strip())
        if value in triangle_dict:
            triangle_word_count += 1

print(triangle_word_count)
