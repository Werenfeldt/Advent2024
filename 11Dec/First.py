stones = list()
modified = list()

def firstRuleApply(st):
    if st == 0:
        print("first rule")
        return True
    return False


def secondRuleApply(st):
    tmp = str(st)
    if len(tmp) % 2 == 0:
        print("second rule")
        return True
    return False



with (open("input/testTwo.txt", 'r') as file):
    for line in file:
        stones = list(map(int, list(line.strip().split(" "))))
print(stones)
for _ in range(2):
    print(stones)
    for stone in stones:
        if firstRuleApply(stone):
            modified.append(1)
        elif secondRuleApply(stone):
            tmp = str(stone)
            mid = len(tmp) // 2
            fst = int(tmp[:mid])
            snd = int(tmp[mid:])
            modified.append(fst)
            modified.append(snd)
        else:
            print("third rule")
            modified.append(stone * 2024)
    print("next loop")
    stones = modified.copy()


print(modified)


