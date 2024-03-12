trojki = []
file_length = 0

def Liczbapierwsza(liczba):

    if liczba > 1:
        for j in range (2,liczba):
            if liczba % j == 0:
                return False
            else:
                return True

    else:
        return False

with open("trojki.txt") as file:
    for line in file:
        file_length += 1
        line = line.strip()
        trojka = line.split(" ")
        trojki.append(trojka)

i = 0

print("Trójki, których pierwsza i druga cyfra sa liczbamy pierwszymi i iloczyn rowna się osatniej:")

while i<file_length:

     liczby = trojki[i]

     liczba1 = int(liczby[0])
     liczba2 = int(liczby[1])

     if Liczbapierwsza(liczba1) and Liczbapierwsza(liczba2):
         if liczba1 * liczba2 == int(liczby[2]):
             print(liczby)

     i += 1




