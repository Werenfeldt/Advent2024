with open("input/input.txt", 'r') as file:
    first = list()
    second = dict()
    for line in file: 
        f,s = line.split()
        first.append(f)
        if second.__contains__(s):
            temp = second.get(s)
            second.update({s: temp + 1})
        else: 
            second[s] = 1 
    total = 0
    for number in first:
        if second.__contains__(number):
            total += int(number) * second.get(number)

    print(total)