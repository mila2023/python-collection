import random
def stworz_plansze(w,k):
    C = [["*"]*k for i in range(w)]
    C[w-1][k-1] = ""
    return C

def narysuj_plansze(C):
    print(" ", end=" ")
    for i in range(len(C[0])):
        print(i, end=" ")
    print("")
    for i in range(len(C)):
        print(i, end=" ")
        for j in range(len(C[0])):
            print(C[i][j], end=" ")
        print("")

def wczytaj_ruch(ostatni,w,k):
    while 1 > 0:
        ww = int(input("Podaj wiersz: "))
        kw = int(input("Podaj kolumnę: "))
        if ww == 0 and kw == 0:
            return 1,0,0
        if ww < ostatni[0] or kw < ostatni[1]:
            if w > ww >= 0 and k > kw >= 0:
                return 0,ww,kw
        print("Niepoprawny ruch! Spróbuj ponownie.")

def wykonaj_ruch(C,ww, kw):
    for i in range(ww, len(C) ):
        for j in range(kw, len(C[0])):
            if C[i][j] == "":
                 break
            C[i][j] = ""
    narysuj_plansze(C)

def rand(C, ostatni):
    if ostatni[1] == 0:
        
    a = random.randint()

def main():
    w = int(input("Podaj liczbe wierszy: "))
    k = int(input("Podaj liczbe kolumn: "))
    l = int(input("Podaj liczbe graczy ludzkich: "))
    if l > 2 or l < 0:
        raise ValueError("Gra jest zero, jedno lub dwuosobowa!")
    C = stworz_plansze(w,k)
    print("Stan planszy: ")

    narysuj_plansze(C)
    ostatni = w-1,k-1
    g = 1

    while 1 > 0:
        print(f"Ruch gracza {g}")
        if l == 0 or ( l == 1 and g == 2):
            ran = rand()
            print(f"Gracz komputerowy bierze kostkę {rand(C,ostatni)}")
            wykonaj_ruch(C, ran[0], ran[1])
        elif l == 2 or (l == 1 and g == 1):
            krotka = wczytaj_ruch(ostatni,w,k)
            ostatni = krotka[1], krotka[2]
            if krotka[0] == 1:
                if g == 1:
                    print(f"Koniec gry, wygrał gracz 2!")
                else:
                    print(f"Koniec gry, wygrał gracz 1!")
                break
            wykonaj_ruch(C,krotka[1], krotka[2])
        if g == 1:
            g = 2
        else:
            g = 1



if __name__=="__main__":
    main()