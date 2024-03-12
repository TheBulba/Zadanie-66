trojki = []
file_length = 0

with open("trojki.txt") as file:
    for line in file:
        file_length += 1
        line = line.strip()
        trojka = line.split(" ")
        trojki.append(trojka)

i = 0
max = 0
poz = 0

print("Najdluzysz trojkat:")

while i<file_length:

    liczby = trojki[i]

    a = int(liczby[0])
    b = int(liczby[1])
    c = int(liczby[2])

    if a**2 + b**2 == c**2:
        if c > max:
            max = c
            poz = i

    i += 1

print(trojki[poz])
