map = list()
start = (0,0)

def printMap():
    for row in map:
        for el in row:
            print(el, end="")
        print()
    

with open("input/test.txt", 'r') as file:
    for x, line in enumerate(file):
        line = list(line.strip())
        if "^" in line:
            start = (x, line.index("^"))

        map.append(line)
    (x,y) = start
    print(start, " - ", map[x][y])
    printMap()


