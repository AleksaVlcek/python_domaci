def unos():
    linije = list(map(int, input().split(",")))
    vreme = list(map(int, input().split(":")))
    if not (0 <= vreme[0] <= 23 and 0 <= vreme[1] <= 59):
        return None
    polasci = []
    x = input()
    while x != "":
        x = list(x.split(","))
        x[0] = int(x[0])
        x[2] = list(map(int, x[2].split(":")))
        if not (0 <= x[2][0] <= 23 and 0 <= x[2][1] <= 59):
            return None
        polasci.append(x)
        x = input()
    print(linije, vreme, polasci)
    return linije, vreme, polasci

def filter(linije, vreme, polasci):
    i = 0
    while i < len(polasci):
        if polasci[i][0] in linije and (polasci[i][2][0] > vreme[0] or (polasci[i][2][0] == vreme[0] and polasci[i][2][1] > vreme[1])):
            i += 1
        else:
            polasci.pop(i)

def obrada(linije, polasci):
    valja = []
    for i in range (len(polasci)):
        if polasci[i][0] in linije:
            valja.append(polasci[i])
    x = []
    if valja != []:
        x = valja[0]
        for i in range (1, len(valja)):
            if valja[i][2][0] < x[2][0] or (valja[i][2][0] == x[2][0] and polasci[i][2][1] < x[2][1]):
                x = valja[i]
    return x

def ispis(polasci, resenje):
    print(len(polasci))
    if resenje == []:
        print("Nema autobusa.", end="")
    else:
        if resenje[2][0] < 10:
            resenje[2][0] = "0" + str(resenje[2][0])
        if resenje[2][1] < 10:
            resenje[2][1] = "0" + str(resenje[2][1])
        print("{}-{} ({}:{})".format(resenje[0], resenje[1], resenje[2][0], resenje[2][1]), end="")


x = unos()
if x != None:
    filter(x[0], x[1], x[2])
    ispis(x[2], obrada(x[0], x[2]))
