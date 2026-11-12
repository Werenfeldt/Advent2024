finalresult = 0
def calc(rest, acul, result):
    global finalresult
    print("acul:", acul)
    if len(rest) == 0 or result in acul:
        print(result)
        if result in acul:
            print("result found ")
            finalresult += result
    else:
        newnum = int(rest[0])
        newAcul = list()
        for a in acul:
            b = a + newnum
            c = a * newnum
            print(a, "+", newnum, "= ", b)
            print(a, "*", newnum, "= ", c)
            newAcul.append(b)
            newAcul.append(c)
        print("newAcul", newAcul)
        print(rest[1:])
        calc(rest[1:], newAcul, result)

with (open("input/input.txt", 'r') as file):
    for line in file:
        number , line = line.split(":")
        line = list(line.strip().split(" "))
        print("trying to find: ", number)
        print("by calcing: ", line)
        acul = [int(line[0])]
        calc(line[1:], acul ,int(number))

        print(finalresult)

## too low: 39629488989532 right answer: 42283209483350