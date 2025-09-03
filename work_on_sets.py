
def podaj():
    rozmiar= int(input("Podaj rozmiar zboiru A\n"))
    lista = ['NaN']*rozmiar
    print("Podaj elementy zbioru A:\n")
    for i in range(rozmiar):
        lista[i] = int(input(f"Podaj ilość {i}: "))
    return lista

def wypisz(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    multi = ["NaN"]*suma
    k = 0
    for i in range(len(lista)):
        for j in range(0,lista[i],1):
            multi[k] = i
            k += 1
    return multi

def dodaj(lista,el):
    if el < len(lista):
        lista[el] += 1
        return wypisz(lista), lista
    else:
        listanowa = [0]*max(len(lista),el+1)
        for i in range(len(lista)):
            listanowa[i] = lista[i]
        listanowa[el] += 1
        return wypisz(listanowa), listanowa

def przeciecie(listaA,listaB):
    minn = min(len(listaA), len(listaB))
    przec = [0]*minn
    for i in range(minn):
        przec[i] = min(listaA[i],listaB[i])
    return wypisz(przec)

def roznica(listaA,listaB):
    if len(listaA) > len(listaB):
        i = len(listaB)-1
        while i >= 0:
            if listaA[i] > listaB[i]:
                listaA[i] -= listaB[i]
            else:
                listaA[i] = 0
            i -= 1
        listawyn = listaA.copy()
    else:
        k = len(listaA)-1
        while k >= 0 and listaA[k] <= listaB[k]:
            k -= 1
        if k == -1:
            listawyn = [0]
        else:
            listawyn = [0]*(k+1)
            for i in range(k, -1, -1):
                if listaA[i] <= listaB[i]:
                    listawyn[i] = 0
                else:
                    listawyn[i] = (listaA[i]-listaB[i])
    return wypisz(listawyn)

def main():

    lista = podaj()
    print(f"Podany zbiór to:\n{wypisz(lista)}")
    el = int(input("Podaj nowy element zbioru A\n"))
    LISTAiMULTI = dodaj(lista,el)
    print(f"Zbior A po dodaniu elementu:\n{LISTAiMULTI[0]}")
    rozmiar2 = int(input("Podaj rozmiar zbioru B\n"))
    print("Podaj elementy zbioru B:\n")
    lista2 = ['NaN'] * rozmiar2
    for i in range(rozmiar2):
        lista2[i] = int(input(f"Podaj ilość {i}: "))
    print(f"Przeciecie zbiorow:\n{przeciecie(LISTAiMULTI[1],lista2)}")
    print(f"Roznica zbiorow:\n{roznica(LISTAiMULTI[1], lista2)}")

if __name__=="__main__":
    main()