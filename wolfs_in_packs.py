import random
import math
def symulacja(p1,p2,k,iledni):
    licznik1 = 0
    licznik2 = 0
    for i in range(iledni):
        ile1 = random.random()
        ile2 = random.random()
        wilki1 = 0
        wilki2 = 0

        if ile1 <= p1:
            wilki1 += 1

        if licznik1 == 2:
            wilki1 += 1
            licznik1 = 0

        if wilki1 == 0:
            licznik1 += 1
        else:
            licznik1 = 0

        # if licznik1 == 2:
        #     wilki1 = 1
        #     licznik1 = 0
        #
        # if ile1 <= p1:
        #     wilki1 += 1
        #     licznik1 = 0
        # elif ile1 > p1:
        #     licznik1 += 1

        print(licznik1, " ", ile1, " ", wilki1)

        if ile2 <= p2:
            wilki2 += 1

        if licznik2 == 2:
            wilki2 += 1
            licznik2 = 0

        if wilki2 == 0:
            licznik2 += 1
        else:
            licznik2 = 0

        # if licznik2 == 2:
        #     wilki2 = 1
        #     licznik2 = 0
        #
        # if ile2 <= p2:
        #     wilki2 += 1
        #     licznik2 = 0
        # else:
        #     licznik2 += 1

        #print(licznik2, " ", ile2, " ", wilki2)
        #print(f"suma1 = {suma1}    suma2 = {suma2}")
        #print("\n")

    print(f"Stado 1 upolowało {polowanie(wilki1,wilki2,k)/iledni} zajęcy/dzień a stado 2: {polowanie(wilki2,wilki1,k)/iledni} zajęcy/dzień.")

def polowanie(s,r,k):
    suma = 0
    random.seed(202121)
    if s == 0 and r == 0:
        suma += k
    elif s == r:
        suma += 5
    elif s > r:
        suma += random.randint(30, 50)
    else:
        suma += random.randint(5, 20)
def tabela(r,k):
    t1 = random.randint(-r,r)
    t2 = random.randint(-r,r)
    p1 = 1/(1+math.exp((-5*t1)/2*r+1))
    p2 = 1/(1+math.exp((-5*t2)/2*r+1))




def p_ataku(t,r):

def main():

    #n_dni - ile dni wychodzą z kazdej
    #p1 - prawdopodobienstwo że zostanie wysłany jeden wilk w 1 stadzie
    #p2 - prawdopodobienstwo że zostanie wysłany jeden wilk w 2 stadzie

    wybor = 0
    while wybor < 3:
        wybor = int(input("Co chcesz zrobić? (1 - Symulacja, 2 - Tabela, 3 - Koniec): "))
        if wybor == 1:
            p1 = 0.9#float(input("Podaj p1: "))
            p2 = 0.15#float(input("Podaj p2: "))
            k = 10#int(input("Podaj k: "))
            iledni = 200#int(input("Podaj liczbę dni: "))
            if p1<0 or p1>1 or p2<0 or p2>1 or k//1!=k or k < 1 or iledni//1!=iledni or iledni<1:
                raise ValueError("Niepoprawna wartość")
            else:
                symulacja(p1,p2,k,iledni)
        else:
            r = int(input("Podaj r: "))
            k = int(input("Podaj k: "))
            tabela(r,k)

if __name__=="__main__":
    main()