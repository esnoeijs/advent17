
"""
 5 1 9 5
 7 5 3
 2 4 6 8
 The first row's largest and smallest values are 9 and 1, and their difference is 8.
 The second row's largest and smallest values are 7 and 3, and their difference is 4.
 The third row's difference is 6.
"""
def part1(text):
    return sum(abs(max(rowInts) - min(rowInts)) for rowInts in (list(map(int, row)) for row in (line.split() for line in text.split("\n"))))

with open("data/day2input.txt") as file:
    print(part1(file.read()))