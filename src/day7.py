class Program:
    children = []
    tag = None

    def __init__(self, tag):
        self.children = []
        self.tag = tag

    def add_child(self, tag):
        self.children.append(tag)


def parse_text(lines):
    programs = []
    for line in lines:
        parts = line.split()
        program = Program(parts[0])
        for child in parts[3:]:
            program.add_child(child.rstrip(','))
        programs.append(program)

    return programs

def find_root_program(programs):
    root = None

    # fix this, too much looping
    for p2 in programs:
        for program in programs:
            if root == None or root.tag in program.children:
                root = program

    return root

#
# with open("data/day7test_input.txt") as file:
#     programs = parse_text(file.read().split("\n"))
#     for p in programs:
#         print(p.tag, p.children)
#
#     root = find_root_program(programs)
#     print(root.tag)

with open("data/day7input.txt") as file:
    programs = parse_text(file.read().split("\n"))
    for p in programs:
        print("%s: %s" % (p.tag, p.children))

    root = find_root_program(programs)
    print(root.tag)
