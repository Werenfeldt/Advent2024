rules = dict()

recheck = list()

with open("input/test.txt", 'r') as file:
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
                for ru in r:
                    if ru in elementsAfter:
                        print("in after: ", ru)
                        jdx = updates.index(ru)
                        print("jdx: ", jdx)
                        print("ru: ", ru, "needs to be before, ", el)
                        tmp = updates.copy()
                        tmp.remove(el)
                        tmp.insert(jdx, el)
                        print("new order: ", tmp)
                        recheck.append(tmp)
                        break

            if passes:
                print("passes: ", updates)


        if not readUpdates:
            key, value = line.strip().split("|")
            #print(key, "|", value)
            rule = rules.get(key)
            if not rule:
                rule = list()
            rule.append(value)
            rules[key] = rule

print(recheck)

#print(rules)
