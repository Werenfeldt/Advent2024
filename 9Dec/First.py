stringlst = list()

with (open("input/input.txt", 'r') as file):
    for line in file:
        lst = list(line.strip())
        #print(lst)
        isFreeSpace = False
        index = 0
        for x in lst:
            print("X: ", x, "index: ", index, "isFreeSpace: ", isFreeSpace)
            if isFreeSpace:
                index += 1
                for _ in range(int(x)):
                    stringlst.append(".")
                isFreeSpace = False
            else:
                for _ in range(int(x)):
                    stringlst.append(index)
                isFreeSpace = True

#print(stringlst)

lookAtIndex = len(stringlst)-1

for idx, space in enumerate(stringlst):
    if idx+1 == lookAtIndex:
        break
    if space == ".":
        found = False
        looking = ""
        while not found:
            looking = stringlst[lookAtIndex]
            if looking != ".":
                found = True
            else:
                lookAtIndex -= 1
        stringlst[idx] = looking
        stringlst[lookAtIndex] = "."

#print(stringlst)
result = 0

for idx, space in enumerate(stringlst):
    if idx+1 == lookAtIndex:
        break
    sum = idx * int(space)
    result += sum
print(result)

#too low:
#91558461993
#6607511583593
