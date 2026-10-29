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

# def searchMiddle(idx, jdx, xmas):
#     number = 0
#     ##Right
#     if grid[jdx][idx:4] == xmas:
#         number += 1
#     ##Left
#     if grid[jdx][idx:idx-4] == xmas:
#         number += 1
#     ##Down
#     if grid[jdx:4][idx] == xmas:
#         number += 1
#     ##Up
#     if grid[jdx:jdx-4][idx] == xmas:
#         number += 1
    

# def searchDiagonal(idx, jdx, xmas):
#     number = 0
#     #UpRight
#     upRight = grid[idx][jdx]+grid[idx+1][jdx-1]+grid[idx+2][jdx-2]+grid[idx+3][jdx-3]
#     if upRight == xmas:
#         number += 1
#     downRight = grid[idx][jdx]+grid[idx+1][jdx+1]+grid[idx+2][jdx+2]+grid[idx+3][jdx+3]
#     if downRight == xmas:
#         number += 1
#     upLeft = grid[idx][jdx]+grid[idx-1][jdx-1]+grid[idx-2][jdx-2]+grid[idx-3][jdx-3]
#     if upLeft == xmas:
#         number += 1
#     downLeft = grid[idx][jdx]+grid[idx-1][jdx+1]+grid[idx-2][jdx+2]+grid[idx-3][jdx+3]
#     if (upLeft == xmas):
#         number += 1

def start():
    min = 4
    max = len(grid[0])-4
    print("MAX", max)
    end = len(grid)
    number = 0
    for idx in range(len(grid[0])):
        for jdx in range(len(grid)):
            print(idx, ",", jdx)
            if idx <= end-min:
                #print("not last 4 colums: ", idx)
                number += down(idx, jdx)
                if jdx >= min-1:
                    number += downLeft(idx, jdx)
                if jdx <= end-min:             
                    number += downRight(idx, jdx)  
            if idx >= min:                
                #print("not first 4 colums: ", idx)
                number += up(idx, jdx)                
                if jdx >= min-1:
                    number += upLeft(idx, jdx)
                if jdx <= end-min:             
                    number += upRight(idx, jdx)  

            if jdx >= min-1:
                #print("not first 4 rows", jdx)
                number += left(idx, jdx)
            if jdx <= end-min:
                #print("not last 4 rows")
                number += right(idx, jdx)
            

            # #Corners
            # if idx == 0 and jdx < min:
            #     print("Corner 1 line: ", idx, "row: ", jdx)
            #     number += down(idx, jdx) + right(idx, jdx) + downRight(idx, jdx)
            # elif idx == 0 and jdx > max:
            #     print("Corner 2 line: ", idx, "row: ", jdx)
            #     number += left(idx, jdx) + down(idx, jdx) + downLeft(idx, jdx)
            # elif idx == end and jdx < min:
            #     print("Corner 3 line: ", idx, "row: ", jdx)
            #     number += up(idx, jdx) + right(idx, jdx) + upRight(idx, jdx)
            # elif idx == end and jdx > max:
            #     print("Corner 4 line: ", idx, "row: ", jdx)
            #     number += left(idx, jdx) + up(idx, jdx) + upLeft(idx, jdx)
            # #Sides
            # elif idx == 0 and min <= jdx <= max:
            #     print("Side 1 line: ", idx, "row: ", jdx)
            #     number += left(idx, jdx) + right(idx, jdx) + down(idx, jdx) + downRight(idx, jdx) + downLeft(idx, jdx)
            # elif idx == end and min <= jdx <= max:
            #     print("Side 2 line: ", idx, "row: ", jdx)
            #     number += left(idx, jdx) + right(idx, jdx) + up(idx, jdx) + upRight(idx, jdx) + upLeft(idx, jdx)
            # elif jdx == 0 and min <= idx <= end - 5:
            #     print("Side 3 line: ", idx, "row: ", jdx)
            #     number += up(idx, jdx) + down(idx, jdx) + right(idx, jdx) + upRight(idx, jdx) + downRight(idx, jdx)
            # elif jdx == end and min <= idx <= end - 5:
            #     print("Side 4 line: ", idx, "row: ", jdx)
            #     number += up(idx, jdx) + down(idx, jdx) + left(idx, jdx) + upLeft(idx, jdx) + downLeft(idx, jdx)
            # #Middle
            # else:
            #     print("Middle line: ", idx, "row: ", jdx)
            #     number +=  left(idx, jdx) + right(idx, jdx) + up(idx, jdx) + down(idx, jdx) + downRight(idx, jdx) + downLeft(idx, jdx) + upRight(idx, jdx) + upLeft(idx, jdx)
            print("______________________________NUMBER: ", number, "________________________________________________________")
    return number
        

with open("input/test.txt", 'r') as file:
    for line in file:
        grid.append(list(line.strip()))
    print(start())
    # start = 0
    # for idx in range(len(grid[0])):
    #     for jdx in range(len(grid)):
    #         grid[0]
    #         list.


    
#print(*grid, sep='\n')

