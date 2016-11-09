'''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''


def all_perms(elements):
    # this is a generator, you will need to iterate over the object by calling next()
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output_list = []
X = all_perms(number_list)

while True:
    try:
        output_list.append(next(X))
    except:
        break

sorted_list = sorted(output_list)
print(sorted_list[999999])
