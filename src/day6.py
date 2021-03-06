import operator

def part1(banks):
    seen_list = {}
    steps = 0
    while True:
        banks_hash = tuple(banks)
        if banks_hash in seen_list:
            return (steps, steps - seen_list[banks_hash])
        seen_list[banks_hash] = steps
        pointer, value = max(enumerate(banks), key=operator.itemgetter(1))
        banks[pointer] = 0
        steps += 1
        while value > 0:
            pointer += 1
            if (pointer >= len(banks)):
                pointer = 0
            value -= 1
            banks[pointer] += 1



text = [0,2,7,0]
print("p1: %s, P2: %s" % (part1(text)[0], part1(text)[1]))

with open("data/day6input.txt") as file:
    text =  list(map(int, file.read().split()))
    print("p1: %s, P2: %s" % (part1(text)[0], part1(text)[1]))
