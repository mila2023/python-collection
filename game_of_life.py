class GraWZycie:
    __slots__ = ["wymiar", "plansza"]

    def __init__(self, n, zapelnione):
        self.wymiar = n
        self.plansza = [[0]*n for i in range(n)]
        for i in range(len(zapelnione)):
            self.plansza[zapelnione[i][0]][zapelnione[i][1]] = 1

    def __str__(self):
        str = ""
        for i in range(self.wymiar):
            str += f"[{self.plansza[i][0]}"
            for j in range(1, self.wymiar):
                str += f", {self.plansza[i][j]}"
            str += "]\n"
        return str

    def wykonaj_krok(self):
        nowa = [[0]*self.wymiar for i in range(self.wymiar)]
        for i in range(self.wymiar):
            for j in range(self.wymiar):
                s = ile_sasiadow(i,j,self.plansza)
                if self.plansza[i][j] == 0 and s == 3:
                    nowa[i][j] = 1
                elif self.plansza[i][j] == 1 and s != 2 and s != 3:
                    nowa[i][j] = 0
                else:
                    nowa[i][j] = self.plansza[i][j]
        self.plansza = nowa

    def __eq__(self, other):
        if not isinstance(other, GraWZycie):
            return False
        if self.wymiar == other.wymiar:
            for i in range(self.wymiar):
                for j in range(self.wymiar):
                    if self.plansza[i][j] != other.plansza[i][j]:
                        return False
            return True

    def __le__(self, other):
        if not isinstance(self, GraWZycie):
            return False
        if not isinstance(other, GraWZycie):
            return False
        if self.wymiar != other.wymiar:
            return False
        for i in range(self.wymiar**2):
            self.wykonaj_krok()
            if self.plansza == other.plansza:
                return True
        return False

def ile_sasiadow(x, y, plansza):
    if type(plansza) != list or type(plansza[0]) != list or type(plansza[0][0]) != int:
        raise Exception("Bledna plansza")
    n = len(plansza)
    if type(x) != int or x >= n or x < 0:
        raise Exception("Bledny x")
    if type(y) != int or y >= n or y < 0:
        raise Exception("Bledny y")
    nieosiagalne = []
    if x == 0:
        nieosiagalne += [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1]]
    if x == n - 1:
        nieosiagalne += [[x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
    if y == 0:
        nieosiagalne += [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1]]
    if y == n - 1:
        nieosiagalne += [[x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
    osiagalne = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if [x + i, y + j] not in nieosiagalne:
                osiagalne.append([x + i, y + j])
    suma = sum([plansza[wsp[0]][wsp[1]] for wsp in osiagalne])
    return suma

def main():
    gwz = GraWZycie(7, [[2, 0], [2, 1], [2, 2], [1, 2], [0, 1]])
    print(gwz)
    gwz.wykonaj_krok()
    print(gwz)
    gwz1 = GraWZycie(7, [[2, 0], [2, 1], [2, 2], [1, 2], [0, 1]])
    gwz2 = GraWZycie(7, [[1, 2], [2, 0], [2, 2], [3, 1], [3, 2]])
    gwz3 = GraWZycie(7, [[1, 2], [2, 0], [2, 2], [3, 1], [3, 2]])
    print("Równy:", gwz1 == gwz2)
    print("Mniejszy lub równy:", gwz1 <= gwz2)
    print("Równy:", gwz3 == gwz2)
    print("Równy liczbie 5:", gwz1 == 5)
    print("Równy napisowi ayyy:", gwz1 == "ayyy")

if __name__=="__main__":
    main()