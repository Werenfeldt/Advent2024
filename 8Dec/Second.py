from operator import truediv

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
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))
                oriDiffx = x2-x1
                oriDiffy = y2-y1

                acuDiffx = oriDiffx
                acuDiffy = oriDiffy

                stillWithinGrid = True
                while stillWithinGrid:
                    n1x, n1y = x1 - acuDiffx, y1 - acuDiffy
                    n2x, n2y = x2 + acuDiffx, y2 + acuDiffy

                    #print(x1, " - ", acuDiffx, y1, " - ", acuDiffy)
                    #print(x2, " + ", acuDiffx, y2, " + ", acuDiffy)

                    nodeOneAdded = False
                    nodeTwoAdded = False
                    if minX <= n1x < maxX and minY <= n1y < maxY:
                        #print("n1: ", n1x, ",", n1y)
                        antinodes.add((n1x,n1y))
                        nodeOneAdded = True
                    if minX <= n2x < maxX and minY <= n2y < maxY:
                        #print("n2: ", n2x, ",", n2y)
                        antinodes.add((n2x, n2y))
                        nodeTwoAdded = True
                    stillWithinGrid = nodeOneAdded or nodeTwoAdded

                    acuDiffx += oriDiffx
                    acuDiffy += oriDiffy
                #print("done looking")


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
    print(points)
    print(maxY)
    print(maxX)
    getAntinodes()
    #print(antinodes)
    print(len(antinodes))


