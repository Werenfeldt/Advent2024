def checkIncOrDec(IsInc, first, second):
    if IsInc:
        if (first < second):
            return True
        else: 
            return False
    else: 
        if (first > second):
            return True
        else: 
            return False

def checkDiffer(first, second):
        if(abs(first-second) > 0 and abs(first-second) < 4):
            return True
        else:
            return False

def checkIfAllIncOrDec(lst):
    IsInc = lst[0] < lst[1]
    for idx in range(len(lst)-1):
        #print(idx)
        if checkIncOrDec(IsInc, lst[idx], lst[idx+1]):
           continue
        else:
            return False
    return True
        
def checkDifferAll(lst):
    for idx in range(len(lst)-1):
        if checkDiffer(lst[idx], lst[idx+1]):
            continue
        else:
            return False
    return True

def SafeWithRemoveOne(lst):
    for idx in range(len(lst)):
        tmp = lst.copy()
        #print(tmp)
        tmp.pop(idx)
        if(checkIfAllIncOrDec(tmp) and checkDifferAll(tmp)):
            return True
        else: 
            continue
    return False

with open("input/input.txt", 'r') as file: 
    valid = 0
    for line in file: 
        lst = list(map(int,line.split()))
        if (checkIfAllIncOrDec(lst) and checkDifferAll(lst)) or SafeWithRemoveOne(lst):
            valid += 1
        #print("lst: ", lst, " is incOrDec: ", checkIfAllIncOrDec(lst), " maxDiffer: ", checkDifferAll(lst), " isSafeWithRemoveOne: ", SafeWithRemoveOne(lst))
    print(valid)

#686
#692 correct
        