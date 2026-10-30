rules = dict()
number = 0

with open("input/input.txt", 'r') as file:
    readUpdates = False
    for line in file:
        line = line.strip()
        #print(line)

        if line.isspace() or not line:
            readUpdates = True
            continue

        if readUpdates:
            updates = line.strip().split(",")
            updates.reverse()
            #print(updates)
            passes = True
            for idx, el in enumerate(updates):
                elementsAfter = updates[idx+1:]
                #print("Element", el)
                #print("ElementsAfter: ", elementsAfter)
                r = rules.get(el)                
                if not r:
                    continue
                #print("R: ", r)
                for el in r:
                    if el in elementsAfter:
                        print("in after")
                        passes = False
                        break
            if passes:
                print("passes: ", updates)
                number += int(updates[len(updates)//2])


        if not readUpdates:
            key, value = line.strip().split("|")
            #print(key, "|", value)
            rule = rules.get(key)
            if not rule:
                rule = list()
            rule.append(value)
            rules[key] = rule



#print(rules)
print(number)
