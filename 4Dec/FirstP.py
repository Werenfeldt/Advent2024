grid = list()
def right(idx, jdx): 
    print("right: ", end=" ")
    right = grid[idx][jdx]+grid[idx][jdx+1]+grid[idx][jdx+2]+grid[idx][jdx+3]
    print(right)
    if right == "XMAS":
        return 1
    return 0
def left(idx, jdx):     
    print("left: ", end="")
    left = grid[idx][jdx]+grid[idx][jdx-1]+grid[idx][jdx-2]+grid[idx][jdx-3]
    print(left)
    if left == "XMAS":
        return 1
    return 0
def down(idx, jdx):
    print("down:", end=" ")
    down = grid[idx][jdx] + grid[idx+1][jdx] + grid[idx+2][jdx] + grid[idx+3][jdx]
    print(down)
    if  down == "XMAS":
        return 1
    return 0
def up(idx, jdx):    
    print("up: ", end=" ")
    up = grid[idx][jdx] + grid[idx-1][jdx] + grid[idx-2][jdx] + grid[idx-3][jdx]
    print(up)
    if up == "XMAS":
        return 1
    return 0

def upRight(idx, jdx):
    print("up right:", end=" ")
    upRight = grid[idx][jdx]+grid[idx-1][jdx+1]+grid[idx-2][jdx+2]+grid[idx-3][jdx+3]
    print(upRight)
    if upRight == "XMAS":
        return 1
    return 0
def downRight(idx, jdx):
    print("down right:", end=" ")
    downRight = grid[idx][jdx]+grid[idx+1][jdx+1]+grid[idx+2][jdx+2]+grid[idx+3][jdx+3]
    print(downRight)
    if downRight == "XMAS":
        return 1
    return 0
def upLeft(idx, jdx):    
    print("up left:", end=" ")
    upLeft = grid[idx][jdx]+grid[idx-1][jdx-1]+grid[idx-2][jdx-2]+grid[idx-3][jdx-3]
    print(upLeft)
    if upLeft == "XMAS":
        return 1
    return 0
def downLeft(idx, jdx):    
    print("down left:", end=" ")
    downLeft = grid[idx][jdx]+grid[idx+1][jdx-1]+grid[idx+2][jdx-2]+grid[idx+3][jdx-3]
    print(downLeft)
    if (downLeft == "XMAS"):
        return 1
    return 0

def start():
    worldLen = 4
    maxRow = len(grid[0])-4
    print("MAX", maxRow)
    print("worldLen", worldLen)
    maxColumn = len(grid)
    print("maxColumn", maxColumn)
    number = 0
    for idx in range(len(grid)):
        for jdx in range(len(grid[0])):
            print(idx, ",", jdx)
            if idx <= maxColumn-worldLen:
                #print("not last 4 colums: ", idx)
                number += down(idx, jdx)
                if jdx >= worldLen-1:
                    number += downLeft(idx, jdx)
                if jdx <= maxRow:
                    number += downRight(idx, jdx)  
            if idx >= worldLen-1:
                #print("not first 4 colums: ", idx)
                number += up(idx, jdx)                
                if jdx >= worldLen-1:
                    number += upLeft(idx, jdx)
                if jdx <= maxRow:
                    number += upRight(idx, jdx)  

            if jdx >= worldLen-1:
                #print("not first 4 rows", jdx)
                number += left(idx, jdx)
            if jdx <= maxRow:
                #print("not last 4 rows")
                number += right(idx, jdx)

            print("______________________________NUMBER: ", number, "________________________________________________________")
    return number
        

with open("input/input.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))
    print(start())


    
#print(*grid, sep='\n')

