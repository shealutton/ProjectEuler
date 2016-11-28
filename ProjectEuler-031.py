'''In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# Use an equation like:
# p + 5n + 10d + 25q + 50 hd = 100

counter = 0
for p1 in range(0, 201):
    for p2 in range(0, 101):
        if p1 + (p2 * 2) > 200:
            #print('Break', p1, p2)
            break
        for p5 in range(0, 41):
            if p1 + (p2 * 2) + (p5 * 5) > 200:
                break
            for p10 in range(0, 21):
                if p1 + (p2 * 2) + (p5 * 5) + (p10 * 10)> 200:
                    break
                for p20 in range(0, 11):
                    if p1 + (p2 * 2) + (p5 * 5) + (p10 * 10) + (p20 * 20) > 200:
                        break
                    for p50 in range(0, 5):
                        if p1 + (p2 * 2) + (p5 * 5) + (p10 * 10) + (p20 * 20) + (p50 * 50) > 200:
                            break
                        for p100 in range(0, 3):
                            if p1 + (p2 * 2) + (p5 * 5) + (p10 * 10) + (p20 * 20) + (p50 * 50) + (p100 * 100) > 200:
                                break
                            for p200 in range(0, 2):
                                if p1 + (p2 * 2) + (p5 * 5) + (p10 * 10) + (p20 * 20) + (p50 * 50) + \
                                   (p100 * 100) + (p200 * 200) > 200:
                                    break
                                elif p1 + (p2 * 2) + (p5 * 5) + (p10 * 10) + (p20 * 20) + (p50 * 50) + \
                                   (p100 * 100) + (p200 * 200) == 200:
                                    counter += 1
                                    print(counter, p1, p2, p5, p10, p20, p50, p100, p200)
