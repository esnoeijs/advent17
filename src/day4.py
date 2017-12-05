
def part1(text):
    return (list(len(words) == len(set(words)) for words in (phrase.split() for phrase in text.split("\n")))).count(1)

def part2(text):
    return list(
                len(list(''.join(sorted(words)) for words in words)) ==
                len(set(''.join(sorted(words))  for words in words))
                for words in (phrase.split() for phrase in text.split("\n"))
    ).count(1)

with open("data/day4input.txt") as file:
    text = file.read()
    print("p1: %s, p2: %s" % (part1(text), part2(text)))
