Argumenty = [int(x) for x in input("podaj liczby po przecinku\n").split(',')]

min = Argumenty[0]
max = Argumenty[0]
print(Argumenty)
for x in Argumenty:
    if x<min:
        min = x
    if x>max:
        max = x
print("wprowadzono "+str(len(Argumenty))+" liczb")
print("największa: "+str(max))
print("najmniejsza: "+str(min))

