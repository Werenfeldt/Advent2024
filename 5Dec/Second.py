rules = dict()

number = 0

def check(line, ite):
    for idx, el in enumerate(line):
        elementsAfter = line[idx+1:]
        r = rules.get(el)
        if not r:
            continue

        for ru in r:
            if ru in elementsAfter:
                print("in after: ", ru)
                jdx = line.index(ru)
                print("jdx: ", jdx)
                print("ru: ", ru, "needs to be before, ", el)
                tmp = line.copy()
                tmp.remove(el)
                tmp.insert(jdx, el)
                print("new order: ", tmp)
                ite += 1
                line, ite = check(tmp, ite)
                break

    print("this line should pass", line)
    return line, ite
        

with open("input/input.txt", 'r') as file:
    readUpdates = False
    for line in file:
        line = line.strip()

        if line.isspace() or not line:
            readUpdates = True
            continue

        if readUpdates:
            updates = line.strip().split(",")
            updates.reverse()

            linePassed, ite = check(updates, 0)
            print("ite: ", ite)
            middle = int(linePassed[len(linePassed)//2])
            print("middle:", middle)
            if ite != 0:
                number += middle



        if not readUpdates:
            key, value = line.strip().split("|")
            rule = rules.get(key)
            if not rule:
                rule = list()
            rule.append(value)
            rules[key] = rule


print(number)
