class Samolot():
    __slots__ = ["name", "seats", "free_places"]

    def zamien_litere_na_liczbe(self, litera):
        return ord(litera.upper()) - ord('A')

    def zamien_liczbe_na_litere(self, liczba):
        return chr(liczba + ord('A'))

    def __init__(self, name, number_of_rows, number_of_seats_in_row):
        self.name = name
        self.seats = [[0] * number_of_seats_in_row for i in range(number_of_rows)]
        self.free_places = number_of_rows * number_of_seats_in_row

    def __repr__(self):
        str = f'{self.name}\n  '
        for i in range(len(self.seats[0])):
            str += f'{self.zamien_liczbe_na_litere(i)} '
        str += '\n'

        for row_index in range(len(self.seats)):
            str += f'{row_index + 1} '
            for column_index in range(len(self.seats[row_index])):
                str += f'{self.seats[row_index][column_index]} '
            str += f'\n'

        return str

    def rezerwuj_miejsce(self, numer_miejsca):
        row_number = int(numer_miejsca[0]) - 1
        seat_number = self.zamien_litere_na_liczbe(numer_miejsca[1])

        if self.seats[row_number][seat_number] == 1:
            return False
        self.seats[row_number][seat_number] = 1
        self.free_places -= 1
        return True

    def sprawdz_czy_miejsce_wolne(self, place_identifier):
        row_number = int(place_identifier[0]) - 1
        seat_number = self.zamien_litere_na_liczbe(place_identifier[1])

        return self.seats[row_number][seat_number] == 0

    def ilosc_wolnych_miejsc(self):
        return self.free_places

    def skopiuj_samolot_z_rezerwacjami(self, nowa_nazwa):
        kopia = Samolot(nowa_nazwa, len(self.seats), len(self.seats[0]))
        for row_number in range(len(self.seats)):
            for column_number in range(len(self.seats[0])):
                kopia.seats[row_number][column_number] = self.seats[row_number][column_number]
                kopia.free_places -= self.seats[row_number][column_number]

        return kopia

    def __sub__(self, other):
        if len(self.seats) != len(other.seats):
            raise ValueError("Liczba rzędów w obu samolotach musi być taka sama")
        if len(self.seats[0]) != len(other.seats[0]):
            raise ValueError("Liczba siedzeń w obu obu samolotach musi być taka sama")

        kopia = self.skopiuj_samolot_z_rezerwacjami(self.name)
        for row_number in range(len(kopia.seats)):
            for column_number in range(len(kopia.seats[0])):
                rezerwacja_miejsca = 0
                if kopia.seats[row_number][column_number] == 1 and other.seats[row_number][column_number] == 0:
                    rezerwacja_miejsca = 1
                kopia.seats[row_number][column_number] = rezerwacja_miejsca
        return kopia

def main():
    print(f'------------Etap 1-----------------------')
    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)

    print(f'------------Etap 2-----------------------')
    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    print(f"Rezerwacja miejsca 2B zakończkona: {airbus.rezerwuj_miejsce('2b')}")
    print(f"Rezerwacja miejsca 3C zakończkona: {airbus.rezerwuj_miejsce('3C')}")
    print(f"Rezerwacja miejsca 4D zakończkona: {airbus.rezerwuj_miejsce('4D')}")
    print(f"Rezerwacja miejsca 5C zakończkona: {airbus.rezerwuj_miejsce('5C')}")
    print(f"Rezerwacja miejsca 4B zakończkona: {airbus.rezerwuj_miejsce('4B')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    assert not airbus.sprawdz_czy_miejsce_wolne('3A'), 'Miejsce dopiero zostało zarezerwowane'
    assert airbus.sprawdz_czy_miejsce_wolne('4C'), 'Miejsce jeszcze nie zostało zarezerwowane'
    print()
    print(airbus)

    print(f'------------Etap 3-----------------------')
    print(f'Ilość wolnych miejsc w samolocie to: {airbus.ilosc_wolnych_miejsc()}')

    print(f'------------Etap 4-----------------------')
    airbus_kopia = airbus.skopiuj_samolot_z_rezerwacjami('Embraer 190+')
    print(airbus_kopia)

    # Potwierdzenie że głęboka kopia
    # orginalny obiekt nie powinien ulec zmianie
    print(f"Rezerwacja miejsca 1B zakończkona: {airbus_kopia.rezerwuj_miejsce('1B')}")
    print(f"Rezerwacja miejsca 1C zakończkona: {airbus_kopia.rezerwuj_miejsce('1C')}")
    print(f"Rezerwacja miejsca 1D zakończkona: {airbus_kopia.rezerwuj_miejsce('1D')}")
    assert airbus.sprawdz_czy_miejsce_wolne('1B'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1C'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1D'), "Kopia się nie udała"
    print(f'Ilość wolnych miejsc w oryginalnym samolocie to: {airbus.ilosc_wolnych_miejsc()}')
    print(f'Ilość wolnych miejsc w kopii to: {airbus_kopia.ilosc_wolnych_miejsc()}')

    print(airbus)
    print(airbus_kopia)

    print(f'------------Etap 5-----------------------')
    samolot_z_roznica = airbus_kopia - airbus
    print(samolot_z_roznica)

    samolot_z_roznica.rezerwuj_miejsce('5A')
    assert airbus_kopia.sprawdz_czy_miejsce_wolne('5A'), "Nie powinno się zmienić miejsce oryginalne"

if __name__ == "__main__":
    main()
