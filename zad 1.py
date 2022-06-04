import random

selected_number = random.randint(1,51)
print("Zgadnij liczbę")
counter=0
while True:
    input_number = int(input('Podaj liczbę\n'))
    if input_number == -1:
        break
    counter = +1
    if input_number == selected_number:
        print(f'brawo udało ci się zgadnąć liczbę w {counter} próbach')
        break
    if input_number > selected_number:
        print('Podana liczba jest większa niż szukana')
        continue
    if input_number < selected_number:
        print('Podana liczba jest za mała niż szukana')
        continue
