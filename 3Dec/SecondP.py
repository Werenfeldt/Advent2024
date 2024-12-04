import re

with open("input/input.txt", 'r') as file:
    sum = 0
    do = True
    for line in file:
        #print("NEW LIIIIINE: ", line)
        rex = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
        #print(rex)
        for idx in range(len(rex)): 
            if do and "mul" in rex[idx]: 
                x, y = str.split(rex[idx], ",")
                _, first = str.split(x, "mul(")
                second, _ = str.split(y, ")")
                #print(first, second)
                sum += (int(first)*int(second))

            if rex[idx] == "don't()":
                #print("DONT")
                do = False
            elif rex[idx] == "do()":
                #print("DO")
                do = True
            else:
                continue
            
                
    print(sum)
    #101629183 too high
    #100411201