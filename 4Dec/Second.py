def rightMas(idx, jdx):
    return grid[idx-1][jdx-1]=="M" and grid[idx+1][jdx-1]=="M" and grid[idx-1][jdx+1]=="S" and grid[idx+1][jdx+1]=="S"

def leftMas(idx, jdx):
    return grid[idx-1][jdx+1]=="M" and grid[idx+1][jdx+1]=="M" and grid[idx-1][jdx-1]=="S" and grid[idx+1][jdx-1]=="S"

def upMas(idx, jdx):
    return grid[idx-1][jdx-1]=="M" and grid[idx-1][jdx+1]=="M" and grid[idx+1][jdx-1]=="S" and grid[idx+1][jdx+1]=="S"

def downMas(idx, jdx):
    return grid[idx+1][jdx-1]=="M" and grid[idx+1][jdx+1]=="M" and grid[idx-1][jdx-1]=="S" and grid[idx-1][jdx+1]=="S"

def found(idx, jdx, maxCol, maxRow):
    if grid[idx][jdx]=="A" and idx > 0 and jdx > 0 and  idx < maxCol and jdx < maxRow:
        return rightMas(idx, jdx) or leftMas(idx, jdx) or upMas(idx, jdx) or downMas(idx, jdx)
    return False

grid = list()
with open("input/input.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

number = 0
maxCol = len(grid)-1
maxRow = len(grid[0])-1
print("MaxCol:", maxCol)
print("MaxRow:", maxRow)
for idx in range(len(grid)):
    for jdx in range(len(grid[0])):
        print(idx, jdx)
        if found(idx, jdx, maxCol, maxRow):
            print("FOUND at: ", idx, ",", jdx)
            number += 1
    print("_____________________________")
print(number)
#print(*grid, sep='\n')