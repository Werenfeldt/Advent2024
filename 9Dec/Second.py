stringlst = list()

def printString():
    for (type,amount) in stringlst:
        for i in range(amount):
            print(type, end='')

    print()

with (open("input/input.txt", 'r') as file):
    for line in file:
        lst = list(line.strip())
        #print(lst)
        isFreeSpace = False
        index = 0
        for x in lst:
            #print("X: ", x, "index: ", index, "isFreeSpace: ", isFreeSpace)
            if isFreeSpace:
                index += 1
                if x != "0":
                    stringlst.append((".", int(x)))
                isFreeSpace = False
            else:

                stringlst.append((index, int(x)))
                isFreeSpace = True

print(stringlst)
printString()

def modify():
    idx = len(stringlst)-1
    while idx >= 0:
        (checkT, checkAmount) = stringlst[idx]
        #print("checkT: ", checkT, "checkAmount: ", checkAmount)
        if checkT != ".":
            for jdx in range(len(stringlst)):
                (t,amount) = stringlst[jdx]

                #print("jdx: ", jdx, "t: ", t, "amount: ", amount)

                if t == "." and amount == checkAmount:
                    #print("amount equal")
                    stringlst[jdx] = (checkT,checkAmount)
                    stringlst[idx] = (t, checkAmount)
                    #print(stringlst)
                    break
                elif t == "." and amount > checkAmount:
                    #print("amount above")
                    stringlst[idx] = (t, checkAmount)
                    stringlst[jdx]= (checkT,checkAmount)
                    stringlst.insert(jdx+1, (".", amount-checkAmount))
                    #print(stringlst)
                    idx += 1
                    break
                elif jdx == idx:
                    #print("wont go further")
                    break
        idx -= 1

modify()
printString()
result = 0
i = 0
for (type,amount) in stringlst:
    #print("i: ", i, "type: ", type, "amount: ", amount)
    if type != ".":
        for j in range(amount):
            #print(result, " + ", type, "*", (j + i))
            result += type * (j + i)
    i += amount
print(result)

#answer: 6636608781232
