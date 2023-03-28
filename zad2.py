import random

Miasta = ["Warszawa","Kraków","Wrocław","Łódź","Poznań","Gdańsk","Szczecin","Bydgoszcz","Lublin","Białystok"]

counter = 1;

print("przykłądowy plan wycieczki:")
while Miasta:
    tmp = random.choice(Miasta)
    print(str(counter)+". "+tmp)
    Miasta.remove(tmp)
    counter+=1