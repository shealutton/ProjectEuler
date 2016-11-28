'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'''

# 1. Generate set of possible solutions per perimeter
# 2. Evaluate each option against Pythagorean Theorem
# 3. Add Pythagorean solutions to a list, if list is longer than max, replace max

winning_tuple = (0, 0)  # format = (perimeter, count of solutions)
for perimeter in range(5, 1001):
    possible_leg_set = set()
    for a in range(1,perimeter-1):
        for b in range(1,perimeter-1):
            if a + b <= perimeter - 1:
                c = perimeter - (a + b)
                if not (b, a, c) in possible_leg_set:
                    possible_leg_set.add((a, b, c))

    count = 0
    for item in possible_leg_set:
        if (item[0]**2 + item[1]**2) == item[2]**2:
            count += 1

    if count > winning_tuple[1]:
        winning_tuple = (perimeter, count)
        print(winning_tuple)
