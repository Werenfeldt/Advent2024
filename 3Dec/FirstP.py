import re

with open("input/input.txt", 'r') as file:
    sum = 0
    for line in file:
        #print("NEW LIIIIINE: ", line)
        rex = re.findall("mul[(]\d+,\d+[)]", line)
        #print(rex)
        for mul in rex:         
            print(mul)
            x, y = str.split(mul, ",")
            
            _, first = str.split(x, "mul(")
            second, _ = str.split(y, ")")
            #print(first, second)
            sum += (int(first)*int(second))
    print(sum)

#174103751