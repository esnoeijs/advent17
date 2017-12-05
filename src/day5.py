import copy

def part1(sequence):
    steps = idx = 0
    maximum = len(sequence)
    while -1 < idx < maximum:
        steps += 1
        next_idx = sequence[idx]
        sequence[idx] = next_idx + 1
        idx += next_idx

    return steps

def part2(sequence):
    steps = idx = 0
    maximum = len(sequence)
    while -1 < idx < maximum:
        steps += 1
        next_idx = sequence[idx]
        sequence[idx] = next_idx + (1 if next_idx < 3 else -1)
        idx += next_idx

    return steps

with open("data/day5input.txt") as file:
    text =  list(map(int, file.read().split("\n")))
    text2 = copy.copy(text)
    print("p1: %s, p2: %s" % (part1(text), part2(text2)))
