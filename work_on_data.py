import copy
def wczytaj():
    dane = []
    with open("dane.txt", "r") as f:
        for line in f:
            dane.append(line)
    return dane

def sprawdz_poprawnosc(dane):
    if len(dane) == 0:
        return False
    for i in dane:
        if type(i) != int or i < 0:
            return False
    return True

def podziel(test):
    if sprawdz_poprawnosc(test) == False:
        raise ValueError("Bledne dane!")
    wyn = [[test[0]]]
    i = 1
    t = 0
    while i < len(test):
        if test[i] > test[i-1]:
            wyn[t].append(test[i])
        else:
            t += 1
            wyn.append([test[i]])
        i += 1
    return wyn


def popraw(test):   # tworzy z listy dane listę o wartościach dodatnich
    for i in range(len(test)):
        if int(test[i]) < 0:
            test[i] = -1*int(test[i])
        else:
            test[i] = int(test[i])
    return test

def wypisz(wyn):
    for i in range(len(wyn)):
        print(f"x[ {i} ]:", end="")
        for j in range(len(wyn[i])):
            print(f"    {wyn[i][j]}", end="")
        print("")

def zlacz_posortowane(wyn):
    pom = [[0]*2 for i in range(len(wyn))]
    suma = 0
    maks = 0
    for i in range(len(wyn)):
        pom[i][1] = len(wyn[i])
        if max(wyn[i]) > maks:
            maks = max(wyn[i])
        suma += len(wyn[i])  # przechowauje docelową dkugosc listy wynikowej

    # pom - tablica formatu: na danym indeksie przechowaywany jest:
    # [0]- indeks na ktorym jestesmy podczas sortowania
    # [1]- dlugosc tego ciagu

    lista = []   # koncowa, wynikowa lista
    # min = wyn[0][0]
    # j = 0
    while len(lista) < suma:
        min = maks
        for i in range(len(wyn)):
            if pom[i][0] < pom[i][1]:
                if wyn[i][pom[i][0]] <= min:
                    # print(wyn[i][pom[i][0]])
                    min = wyn[i][pom[i][0]]
                    rzad = i
        lista.append(wyn[rzad][pom[rzad][0]])
        # print(lista)
        # print(wyn[rzad][pom[rzad][0]])
        # print(rzad, "  ", wyn[rzad][pom[[rzad]]])
        pom[rzad][0] += 1
    return lista

# def zlacz_posortowane(wyn):
#     lista = [wyn[0][i] for i in range(len(wyn[0]))]
#     for i in range(1,len(wyn)):
#         for j in range(len(wyn[i])):
#             for k in range(1, len(lista)):
#                 if lista[k-1] <= wyn[i][j] <= lista[k]:
#                     lista[:k] + [wyn[i][j]] + l[k:]
#


def main():

    dane = wczytaj()
    test = dane.copy()
    test = popraw(test)
    # for i in range(len(test)):
    #     print(test[i])
    wyn = podziel(test)
    wypisz(wyn)
    print(zlacz_posortowane(wyn))

if __name__=="__main__":
    main()