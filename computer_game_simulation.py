import random
import math
def mozliwe_akcje():
    print("1 - atak toporem(230 obrazen, 30 % szan na trafienie)")
    print("2 - magiczny pocisk(50 - 100 obrazen, 20 punktow many)")
    print("3 - potezny atak(200 - 400 obrazen, 35 % szans na trafienie, raz na cztery tury)")
    print("4 - zapisz grę")
    print("5 - odczytaj grę")

def wypisz_zycie_trolla(pkt):
    print(f"Troll ma {pkt} pkt. życia")

def pobierz_akcje(pkt, mana, ileminelo3):
    temp = 0
    while temp == 0:
        a = int(input("Wybierz akcję: "))
        if a < 1 or a > 5:
            print("Numer akcji musi być pomiędzy 0 a 5")
        elif a == 2 and mana < 20:
            print("Za mało many.")
        elif a == 3 and ileminelo3 < 3:
            print("Jeszcze za wcześnie na atak 3")
        else:
            temp = 1
    return a

def zapisz_gre(troll, mana, ileminelo3):
    sciezka = input("Podaj ścieżkę do pliku: ")
    with open(sciezka, "w") as plik:
        plik.write(f"{troll}\n{mana}\n{ileminelo3}")


def odczytaj_gre():
   sciezka = input("Podaj ścieżkę do pliku: ")
   with open(sciezka, "r") as plik:
       krotka = plik.readline()[:-1], plik.readline()[:-1], plik.readline()
       print(krotka)
       return krotka


def main():

    pkt = 1000
    mana = 100
    ileminelo3 = 10

    while pkt > 0:
        wypisz_zycie_trolla(pkt)
        mozliwe_akcje()
        a = pobierz_akcje(pkt,mana,ileminelo3)
        if a == 1:
            pkt -= 230
            ileminelo3 += 1
        elif a == 2:
            mana -= 20
            pkt -= random.randint(50,100)
            ileminelo3 += 1
        elif a == 3:
            pkt -= random.randint(200,400)
            ileminelo3 = 0
        elif a == 4:
            zapisz_gre(pkt, mana, ileminelo3)
        else:
            odczytaj_gre()


with open("moj-plik","w") as f:
    f.write("troll\n")

if __name__=="__main__":
    main()