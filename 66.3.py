trojki = []
file_length = 0

with open("trojki.txt") as file:
    for line in file:
        file_length += 1
        line = line.strip()
        trojka = line.split(" ")
        trojki.append(trojka)

i = 0

print("Trojki boków trójkąta prostokątnego:")

while i < file_length:

    liczby = trojki[i]

    a = int(liczby[0])
    b = int(liczby[1])
    c = int(liczby[2])

    if a**2 + b**2 == c**2:
        print(liczby)

    i += 1
