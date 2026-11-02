map = list()
start = (0,0)
visited = dict()
marker = ""
done = False

def checkLeaving(idx, jdx):
    print("checkLeaving")
    global done
    if (len(map)-1 < idx or idx < 0 or len(map[0])-1 < jdx or jdx < 0) and not done :
        print("done: ")
        printMap()
        print(len(visited))
        done = True

def up(idx, jdx):
    (xs,ys) = (idx-1, jdx)
    checkLeaving(xs, ys)

    if not done:
        point = map[xs][ys]
        print("up: ", point, "- (", xs, ", ", ys, ")" )

        if point == "#":
            turnRight(idx, jdx)
        elif (xs, ys) not in visited:
            visited[(xs, ys)] = True

        up(xs, ys)

def down(idx, jdx):

    (xs,ys) = (idx+1, jdx)
    checkLeaving(xs, ys)

    if not done:
        point = map[xs][ys]
        print("down: ", point, "- (", xs, ", ", ys, ")" )
        if point == "#":
            turnRight(idx, jdx)
        elif (xs, ys) not in visited:
            visited[(xs, ys)] = True

        down(xs, ys)

def left(idx, jdx):
    (xs, ys) = (idx, jdx-1)

    checkLeaving(xs, ys)

    if not done:
        print("heeeeeeej")
        point = map[xs][ys]
        print("left: ", point, "- (", xs, ", ", ys, ")")

        if point == "#":
            turnRight(idx, jdx)
        elif (xs, ys) not in visited:
            print("hej med dig")
            visited[(xs, ys)] = True

        left(xs, ys)

def right(idx, jdx):
    (xs,ys) = (idx, jdx+1)
    checkLeaving(xs, ys)

    if not done:
        point = map[xs][ys]
        print("right: ", point, "- (", xs, ", ", ys, ")" )

        if point == "#":
            turnRight(idx, jdx)
        elif (xs, ys) not in visited:
            visited[(xs, ys)] = True

        right(xs, ys)

def turnRight(idx, jdx):
    global marker
    print("turning right")
    if marker == '^':
        marker = '>'
        right(idx, jdx)
    if marker == 'v':
        marker = '<'
        left(idx, jdx)
    if marker == '<':
        marker = '^'
        up(idx, jdx)
    if marker == '>':
        marker = 'v'
        down(idx, jdx)

def printMap():
    for idx, row in enumerate(map):
        for jdx, el in enumerate(row):
            if visited.get((idx, jdx)):
                print("X", end="")
            else:
                print(el, end="")
        print()
    

with open("input/input.txt", 'r') as file:
    for x, line in enumerate(file):
        line = list(line.strip())
        if "^" in line:
            start = (x, line.index("^"))

        map.append(line)
    (x,y) = start
    print(start, " - ", map[x][y])
    print("cols: ", len(map), "rows", len(map[0]))
    visited[(x,y)] = True
    marker = map[x][y]
    map[x][y] = '.'
    if marker == '^':
        up(x, y)
    if marker == 'v':
        down(x, y)
    if marker == '<':
        left(x, y)
    if marker == '>':
        right(x, y)




