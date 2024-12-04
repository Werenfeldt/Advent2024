with open("input/input.txt", 'r') as file:
    first = list()
    second = list()
    for line in file: 
        f,s = line.split()
        first.append(int(f))
        second.append(int(s))
    
    first.sort()
    second.sort()

    total = 0
    for i,number in enumerate(first):
        total += abs(number-second[i])

    print(total)