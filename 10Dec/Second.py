grid = list()

startingpoints = list()

maxCol = 0
maxRow = 0
found = 0
foundSum = 0

def up(x, y, nr):
    xm = x - 1
    if 0 <= xm < maxRow and 0 <= y < maxCol and grid[xm][y] == nr:
        print("found up: (", xm, ",", y, ") : ", nr )
        return True
    return False
def down(x, y, nr):
    xm = x + 1
    if 0 <= xm < maxRow and 0 <= y < maxCol and grid[xm][y] == nr:
        print("found down: (", xm, ",", y, ") : ", nr)
        return True
    return False

def left(x, y, nr):
    ym = y - 1
    if 0 <= x < maxRow and 0 <= ym < maxCol and grid[x][ym] == nr:
        print("found left: (", x, ",", ym, ") : ", nr)
        return True
    return False
def right(x, y, nr):
    ym = y + 1
    if 0 <= x < maxRow and 0 <= ym < maxCol and grid[x][ym] == nr:
        print("found right: (", x, ",", ym, ") : ", nr)
        return True
    return False

def isfound(nr):
    return nr == 9

def check(point):
    global found
    x, y = point
    points = list()
    if 0 <= x < maxRow and 0 <= y < maxCol:
        nr = grid[x][y] + 1
        if up(x, y, nr):
            if isfound(grid[x-1][y]):
                found += 1
            else:
                points.append((x-1, y))
        if down(x, y, nr):
            if isfound(grid[x+1][y]):
                found += 1
            else:
                points.append((x+1, y))
        if left(x, y, nr):
            if isfound(grid[x][y-1]):
                found += 1
            else:
                points.append((x, y-1))
        if right(x, y, nr):
            if isfound(grid[x][y + 1]):
                found += 1
            else:
                points.append((x, y + 1))

    print(points)
    for p in points:
        check(p)



with (open("input/input.txt", 'r') as file):
    for row, line in enumerate(file):
        line = list(map(int, list(line.strip())))
        grid.append(line)
        if 0 in line:
            for idx, x in enumerate(line):
                if x == 0:
                    startingpoints.append((row, idx))

maxCol = len(grid[0])
maxRow = len(grid)

for startingpoint in startingpoints:
    check(startingpoint)
    print(found)
    foundSum += found
    found = 0

print(foundSum)

