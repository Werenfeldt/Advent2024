files = list()
freespace = list()

def printDisk():
    for x, file in enumerate(files):
        for value in range(file):
            print(x, end="")

        if x != len(files) - 1:
            free = freespace[x]
            for space in range(free):
                print(".", end="")

def printFile(id, file):
    for _ in range(file):
        print(id, end="")

def printFreespace(free):
    for _ in range(free):
        print(".", end="")

with (open("input/test.txt", 'r') as file):
    for line in file:
        lst = list(line.strip())
        print(lst)

        for x in range(0, len(lst)-1, 2):
            file = int(lst[x])
            free = int(lst[x+1])
            printFile(x, file)
            print("X", x)

            if x == len(lst)-1:
                print("xxx: ", x+1)
                printFile(x+1, int(lst[-1]))
                break

            printFreespace(free)


print(files)
print(freespace)


