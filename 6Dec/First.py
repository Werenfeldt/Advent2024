map = list()
start = (0,0)
visited = dict()
marker = ""
done = False

def checkLeaving(idx, jdx):
    #print("checkLeaving")
    global done
    if (len(map)-1 < idx or idx < 0 or len(map[0])-1 < jdx or jdx < 0) and not done :
        print("done: ")
        return True
    return False

def up(idx, jdx):
    return (idx-1, jdx)

def down(idx, jdx):
    return (idx+1, jdx)

def left(idx, jdx):
    return (idx, jdx-1)

def right(idx, jdx):
    return (idx, jdx+1)

def turnRight(idx, jdx):
    global marker
    #print("turning right")
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

    while not done:
        idx, jdx = x , y
        #print("xy before: ", x, ", ", y)
        #print("dx before: ", idx, ", ", jdx)
        if marker == '^':
            (x,y) = up(x, y)
        if marker == 'v':
            (x,y) = down(x, y)
        if marker == '<':
            (x, y) = left(x, y)
        if marker == '>':
            (x, y) = right(x, y)

        done = checkLeaving(x,y)
        if done:
            break

        point = map[x][y]

        if point == "#":
            turnRight(idx, jdx)
            x, y = idx, jdx
        elif (x, y) not in visited:
            visited[(x, y)] = True

#printMap()
print(len(visited))


