antinodes = set()
points = dict()

maxY = 0
minY = 0
maxX = 0
minX = 0

def getAntinodes():
    for keys in points.keys():
        values = points[keys]
        for idx, val in enumerate(values):
            #print("first comparing: ", val, end=" ")
            x1, y1 = val
            for i in range(idx+1, len(values)):
                x2, y2 = values[i]
                diffx = x2-x1
                diffy = y2-y1
                n1x, n1y = x1-diffx, y1-diffy
                n2x, n2y = x2+diffx, y2+diffy
                #print("n1: ", n1x, ",", n1y)
                #print("n2: ", n2x, ",", n2y)
                if minX <= n1x < maxX and minY <= n1y < maxY:
                    antinodes.add((n1x,n1y))
                if minX <= n2x < maxX and minY <= n2y < maxY:
                    antinodes.add((n2x, n2y))
                #print("to ", secVal)


with (open("input/input.txt", 'r') as file):
    for x, line in enumerate(file):
        row = list(line.strip())
        #print(row)
        maxY = len(row)
        for y, point in enumerate(row):
            if point != '.':
                lst = points.get(point)
                if lst is None:
                    #print(point, " does not exists in dict")
                    lst = []
                lst.append((x,y))
                points[point] = lst
        maxX += 1
    #print(points)
    #print(maxY)
    #print(maxX)
    getAntinodes()
    print(len(antinodes))


