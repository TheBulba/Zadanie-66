trojki = []
file_length = 0

with open("trojki.txt") as file:
    for line in file:
        file_length += 1
        line = line.strip()
        trojka = line.split(" ")
        trojki.append(trojka)


i = 0

print("Trójki, których suma cyfr pierwszego i drugiego rowna się trzeciemu:")

while i<file_length:
    j1 = 0
    j2 = 0
    suma1= 0
    suma2= 0

    liczby = trojki[i]

    dlug1 = len(liczby[0]) - 1
    dlug2 = len(liczby[1]) - 1

    liczba1 = int(liczby[0])
    liczba2 = int(liczby[1])

    while dlug1 >= 0:
        x1 = liczba1 // (10**dlug1)
        suma1 += x1
        liczba1 = liczba1 - (x1*(10**dlug1))
        dlug1 -= 1
        j1+=1

    while dlug2 >= 0:
        x2 = liczba2 // (10**dlug2)
        suma2 += x2
        liczba2 = liczba2 - (x2*(10**dlug2))
        dlug2 -= 1
        j2+=1


    if suma1 + suma2 == int(liczby[2]):
        print(liczby)

    i+=1
