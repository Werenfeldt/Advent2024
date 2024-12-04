grid = list()

def right(idx, jdx, xmas): 
    if grid[jdx][idx:4] == xmas:
        return 1
    return 0
def left(idx, jdx, xmas): 
    if grid[jdx][idx:idx-4] == xmas:
        return 1
    return 0
def down(idx, jdx, xmas): 
    if grid[jdx:4][idx] == xmas:
        return 1
    return 0
def up(idx, jdx, xmas):
    if grid[jdx:jdx-4][idx] == xmas:
        return 1
    return 0

def upRight(idx, jdx, xmas):
    upRight = grid[idx][jdx]+grid[idx+1][jdx-1]+grid[idx+2][jdx-2]+grid[idx+3][jdx-3]
    if upRight == xmas:
        return 1
    return 0
def downRight(idx, jdx, xmas):
    downRight = grid[idx][jdx]+grid[idx+1][jdx+1]+grid[idx+2][jdx+2]+grid[idx+3][jdx+3]
    if downRight == xmas:
        return 1
    return 0
def upLeft(idx, jdx, xmas):
    upLeft = grid[idx][jdx]+grid[idx-1][jdx-1]+grid[idx-2][jdx-2]+grid[idx-3][jdx-3]
    if upLeft == xmas:
        return 1
    return 0
def downLeft(idx, jdx, xmas):
    downLeft = grid[idx][jdx]+grid[idx-1][jdx+1]+grid[idx-2][jdx+2]+grid[idx-3][jdx+3]
    if (upLeft == xmas):
        return 1
    return 0

def searchMiddle(idx, jdx, xmas):
    number = 0
    ##Right
    if grid[jdx][idx:4] == xmas:
        number += 1
    ##Left
    if grid[jdx][idx:idx-4] == xmas:
        number += 1
    ##Down
    if grid[jdx:4][idx] == xmas:
        number += 1
    ##Up
    if grid[jdx:jdx-4][idx] == xmas:
        number += 1
    

def searchDiagonal(idx, jdx, xmas):
    number = 0
    #UpRight
    upRight = grid[idx][jdx]+grid[idx+1][jdx-1]+grid[idx+2][jdx-2]+grid[idx+3][jdx-3]
    if upRight == xmas:
        number += 1
    downRight = grid[idx][jdx]+grid[idx+1][jdx+1]+grid[idx+2][jdx+2]+grid[idx+3][jdx+3]
    if downRight == xmas:
        number += 1
    upLeft = grid[idx][jdx]+grid[idx-1][jdx-1]+grid[idx-2][jdx-2]+grid[idx-3][jdx-3]
    if upLeft == xmas:
        number += 1
    downLeft = grid[idx][jdx]+grid[idx-1][jdx+1]+grid[idx-2][jdx+2]+grid[idx-3][jdx+3]
    if (upLeft == xmas):
        number += 1

def start():
    min = 4
    max = grid[0][0]-4
    number = 0
    for idx in range(len(grid[0])):
        for jdx in range(len(grid)):
            #Middle
            if min < idx < max and min < jdx < max:
                number +=  left(idx, jdx) + right(idx, jdx) + up(idx, jdx) + down(idx, jdx) + downRight(idx, jdx) + downLeft(idx, jdx) + upRight(idx, jdx) + upLeft(idx, jdx)
            #Sides
            elif min < idx < max and jdx < min:
                number += left(idx, jdx) + right(idx, jdx) + down(idx, jdx) + downRight(idx, jdx) + downLeft(idx, jdx)
            elif min < idx < max and jdx > max:
                number += left(idx, jdx) + right(idx, jdx) + up(idx, jdx) + upRight(idx, jdx) + upLeft(idx, jdx)
            elif idx < min and min < jdx < max:
                number += up(idx, jdx) + down(idx, jdx) + right(idx, jdx) + upRight(idx, jdx) + downRight(idx, jdx)
            elif idx > max and min < jdx < max:
                number += up(idx, jdx) + down(idx, jdx) + left(idx, jdx) + upLeft(idx, jdx) + downLeft(idx, jdx)
            #Corners
            elif idx < min and jdx < min:
                number += down(idx, jdx) + right(idx, jdx) + downRight(idx, jdx)
            elif idx < min and jdx > max:
                number += up(idx, jdx) + right(idx, jdx) + upRight(idx, jdx)
            elif idx > max and jdx < min:
                number += down(idx, jdx) + left(idx, jdx) + downLeft(idx, jdx)
            elif idx > max and jdx > min:
                number += up(idx, jdx) + left(idx, jdx) + upLeft(idx, jdx)
        

with open("input/test.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

    start = 0
    for idx in range(len(grid[0])):
        for jdx in range(len(grid)):
            grid[0]
            list.


    
print(*grid, sep='\n')

