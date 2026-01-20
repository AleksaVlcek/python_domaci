def unos():
    minuti = input().split("-")
    if minuti[0] != "":
        minuti[0] = list(map(int, minuti[0].split(",")))
    else:
        minuti[0] = []
    if minuti[1] != "":
        minuti[1] = list(map(int, minuti[1].split(",")))
    else:
        minuti[1] = []
    for i in minuti:
        for j in i:
            if not 1 <= j <= 90:
                return None
    return minuti

def rez(minuti):
    prvo = [0, 0]
    drugo = [0, 0]
    for i in [0, 1]:
        for j in minuti[i]:
            drugo[i] += 1
            if j <= 45:
                prvo[i] += 1
    print("{}:{} ({}:{})".format(drugo[0], drugo[1], prvo[0], prvo[1]))

def vreme(minuti):
    minuti = minuti[0] + minuti[1]
    if minuti != []:
        start = minuti[0]
        end = minuti[0]
        for i in minuti[1:]:
            if i < start:
                start = i
            if i > end:
                end = i
        print("{}-{}".format(start, end))


minuti = unos()
if minuti != None:
    print(minuti[0])
    print(minuti[1])
    rez(minuti)
    vreme(minuti)