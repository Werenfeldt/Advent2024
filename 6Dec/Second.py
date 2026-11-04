map = list()
start = (0, 0)
visited = dict()
marker = ""
done = False


def checkLeaving(idx, jdx):
    # print("checkLeaving")
    global done
    if (len(map) - 1 < idx or idx < 0 or len(map[0]) - 1 < jdx or jdx < 0) and not done:
        print("done: ")
        return True
    return False

def horiRightCheck(q, z):
    found = False
    for idx in range(z, len(map[q])):
        if map[q][idx] == "#":
            found = True
            break
    return found

def horiLeftCheck(q, z):
    found = False
    idx = z

    while idx <= 0 and not found:
        if map[q][idx] == "#":
            found = True
        idx -= 1
    return found

def horiDownCheck(q, z):
    found = False
    for idx in range(q, len(map)):
        if map[idx][z] == "#":
            found = True
            break
    return found

def horiUpCheck(q, z):
    found = False
    idx = q

    while idx <= 0 and not found:
        if map[idx][z] == "#":
            found = True
        idx -= 1
    return found


def checkRight(idx, jdx):
    global marker

    if marker == '^':
        (a, b) = up(idx, jdx)
    if marker == 'v':
        (a, b) = down(idx, jdx)
    if marker == '<':
        (a, b) = left(idx, jdx)
    if marker == '>':
        (a, b) = right(idx, jdx)

    #print("a,b: ", a, ", ", b)

    if 0 <= a < len(map) and 0 <= b < len(map[0]):
        nextPoint = map[a][b]

        (q,z) = (0,0)
        found = False
        if nextPoint != "#":
            if marker == '^':
                (q,z) = right(idx, jdx)
                if (visited.get((q,z)) == '-' or visited.get((q,z))== '+') and horiRightCheck(q,z):
                    found = True
            elif marker == 'v':
                (q,z) = left(idx, jdx)
                if (visited.get((q,z)) == '-' or visited.get((q,z)) == '+') and horiLeftCheck(q,z):
                    found = True
            elif marker == '<':
                (q,z) = up(idx, jdx)
                if (visited.get((q,z)) == '|' or visited.get((q,z)) == '+') and horiUpCheck(q,z):
                    found = True
            elif marker == '>':
                (q,z) = down(idx, jdx)
                if (visited.get((q,z)) == '|' or visited.get((q,z)) == '+') and horiDownCheck(q,z):
                    found = True

            print("right point: ", visited.get((q,z)))

        if found:
            print("Found: ", a, ", ", b)


def up(idx, jdx):
    return (idx - 1, jdx)


def down(idx, jdx):
    return (idx + 1, jdx)


def left(idx, jdx):
    return (idx, jdx - 1)


def right(idx, jdx):
    return (idx, jdx + 1)


def turnRight(idx, jdx):
    global marker
    # print("turning right")
    if marker == '^':
        marker = '>'
    elif marker == 'v':
        marker = '<'
    elif marker == '<':
        marker = '^'
    elif marker == '>':
        marker = 'v'


def printMap():
    for idx, row in enumerate(map):
        for jdx, el in enumerate(row):
            if visited.get((idx, jdx)):
                print("X", end="")
            else:
                print(el, end="")
        print()


with open("input/test.txt", 'r') as file:
    for x, line in enumerate(file):
        line = list(line.strip())
        if "^" in line:
            start = (x, line.index("^"))
        if "#" in line:
            y = line.index("#")
        
        map.append(line)

    (x, y) = start
    print(start, " - ", map[x][y])
    print("cols: ", len(map), "rows", len(map[0]))
    visited[(x, y)] = '|'
    marker = map[x][y]
    map[x][y] = '.'

    while not done:
        idx, jdx = x, y
        # print("xy before: ", x, ", ", y)
        # print("dx before: ", idx, ", ", jdx)
        if marker == '^':
            (x, y) = up(x, y)
        if marker == 'v':
            (x, y) = down(x, y)
        if marker == '<':
            (x, y) = left(x, y)
        if marker == '>':
            (x, y) = right(x, y)

        done = checkLeaving(x, y)
        if done:
            break

        point = map[x][y]

        checkRight(x, y)

        if point == "#":
            turnRight(idx, jdx)
            x, y = idx, jdx
        elif (x, y) not in visited:
            if marker == '^' or marker == 'v':
                visited[(x, y)] = '|'
            else:
                visited[(x, y)] = '-'
        elif (x, y) in visited:
            visited[(x,y)] = '+'




# printMap()
print(len(visited))


