import random

rounds = input("wpisz ilość rund\n")
gamemode = input('"0" - komputer "1" - hot seats\n')
PossibleInput = [0,1,2]
matchResolve = 0
p1Win = 0
p2Win = 0

#0=papier 1=kamien 2=nożyce
def match(x1,x2):
    resolve = 0
    p1=int(x1)
    p2=int(x2)
    if p1==p2:
        print("[remis]")
        resolve = 0
    elif (p1 == 0 and p2 == 1)or(p1 == 1 and p2 == 2)or(p1 == 2 and p2 == 0):
        print("[p1 wygrywa]")
        resolve = 1
    elif (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
        print("[p2 wygrywa]")
        resolve = 2
    #0-remis 1-gracz1 2-gracz2
    return resolve

if gamemode=="0":
    print("gra z komputerem:\n")
    for x in range(int(rounds)):
        tmpInput = input("wpisz 0,1,2 ==> papier,kamień,nożyce\n")
        matchResolve = match(tmpInput,random.choice(PossibleInput))

if gamemode=="1":
    print("gra z przeciwnikiem:\n")
    for x in range(int(rounds)):
        tmpInput1 = input("P1 wpisz 0,1,2 ==> papier,kamień,nożyce\n")
        tmpInput2 = input("P2 wpisz 0,1,2 ==> papier,kamień,nożyce\n")
        matchResolve = match(tmpInput1,tmpInput2)

if p1Win==p2Win:
    print("REMIS")
elif p1Win>p2Win:
    print("P1 WYGRYWA")
elif p2Win>p1Win:
    print("P2 WYGRYWA")
print("SCORE:")
print("P1: "+str(p1Win)+" WIN/S ___________ "+"P2: "+str(p2Win)+"WIN/S")
