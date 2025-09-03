class Samolot():
    __slots__ = ["nazwa", "siedzenia", "mwolne"]

    def __init__(self, nazwa, lrzedow, mwrzedzie):  # init - konstruktor
        self.nazwa = nazwa
        self.siedzenia = [[0] * mwrzedzie for i in range(lrzedow)]
        self.mwolne = lrzedow * mwrzedzie

    def __str__(self):  # zamiast __repr__
        # pass
        # return f"{self.nazwa} \n  {ord(i+65) for i in range(self.siedzenia[0])} {self.siedzenia}"
        # print(f"Samolot(miejsca,cokolwiek)")
        str = f"{self.nazwa}\n  "
        for i in range(len(self.siedzenia[0])):
            str += f"{self.liczlit(i)} "
        str += "\n"
        for i in range(len(self.siedzenia)):
            str += f"{i+1} "
            for j in range(len(self.siedzenia[0])):
                str += f"{self.siedzenia[i][j]} "
            str += "\n"
        return str

    def litlicz(self, litera):
        return ord(litera.upper()) - ord('A')

    def liczlit(self, liczba):
        return chr(liczba + ord('A')) #ord() - zamienia znak na ascii

    def rezerwuj_miejsce(self, nr):
        wiersz = int(nr[0]) - 1
        kolumna = self.litlicz(nr[1])  # 'A' = 0
        if self.siedzenia[wiersz][kolumna] == 1:
            return False
        else:
            self.siedzenia[wiersz][kolumna] = 1
            self.mwolne -= 1
            return True

    def sprawdz_czy_miejsce_wolne(self, nr):
        wiersz = int(nr[0]) - 1
        kolumna = self.litlicz(nr[1])
        if self.siedzenia[wiersz][kolumna] == 1:
            return False
        else:
            return True

    def ilosc_wolnych_miejsc(self):
        return self.mwolne

    def skopiuj_samolot_z_rezerwacjami(self, nnazwa):
        kopia = Samolot(nnazwa, len(self.siedzenia), len(self.siedzenia[0]))
        for i in range(len(self.siedzenia)):
            for j in range(len(self.siedzenia[0])):
                kopia.siedzenia[i][j] = self.siedzenia[i][j]
        kopia.mwolne = self.mwolne
        return kopia


    def __sub__(self, other):
        if len(self.siedzenia) != len(other.siedzenia):
            raise ValueError("Samoloty nie są porownywalnej wielkosci")
        if len(self.siedzenia[0]) != len(other.siedzenia[0]):
            raise ValueError("Samoloty nie są porownywalnej wielkosci")

        samolot_z_roznica = Samolot(self.nazwa, len(self.siedzenia), len(self.siedzenia[0]))
        for i in range(len(self.siedzenia)):
            for j in range(len(self.siedzenia[0])):
                if self.siedzenia[i][j] == 0 or (self.siedzenia[i][j] == 1 and other.siedzenia[i][j] != 1):
                    samolot_z_roznica.siedzenia[i][j] = self.siedzenia[i][j]
        return samolot_z_roznica


def main():
    print(f'------------Etap {1}-----------------------\n')
    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)

    print(f'------------Etap {2}-----------------------\n')
    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    print(f"Rezerwacja miejsca 2b zakończkona: {airbus.rezerwuj_miejsce('2b')}")
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

    print(f'------------Etap 3-----------------------\n')
    print(f'Ilość wolnych miejsc w samolocie to: {airbus.ilosc_wolnych_miejsc()}')

    print(f'------------Etap 4-----------------------\n')
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
