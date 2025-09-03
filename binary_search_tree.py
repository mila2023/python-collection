class BST:
    """Implementacja drzewa poszukiwań binarnych"""
    __slots__ = ["korzen"]
    class Node:
        __slots__ = ["klucz", "lewy", "prawy"]
        def __init__(self, klucz, lewy, prawy):
            self.klucz = klucz
            self.lewy = lewy
            self.prawy = prawy

    def __init__(self):
        self.korzen = None

    def czy_pusty(self):
        return (self.korzen is None)

    def czy_istnieje(self, klucz):
        akt = self.korzen
        while akt is not None:
            if akt.klucz == klucz:
                return True
            elif klucz < akt.klucz:  # idź w lewo
                akt = akt.lewy
            else:  # idź w prawo
                akt = akt.prawy
        return False

    def czy_istnieje_rek(self, klucz):
        def _czy_istnieje(akt):
            if akt is None:
                return False
            elif akt.klucz == klucz:
                return True
            elif klucz < akt.klucz:  # idź w lewo
                return _czy_istnieje(akt.lewy)
            else:  # idź w prawo
                return _czy_istnieje(akt.prawy)
        return _czy_istnieje(self.korzen)

    def wstaw(self, klucz):
        if self.korzen is None:
            self.korzen = BST.Node(klucz, None, None)
        else:
            akt = self.korzen
            while True:
                if akt.klucz == klucz:
                    return  # bez duplikatów
                elif klucz < akt.klucz:
                    if akt.lewy is None:
                        akt.lewy = BST.Node(klucz, None, None);
                        return
                    else:
                        akt = akt.lewy
                else:
                    if akt.prawy is None:
                        akt.prawy = BST.Node(klucz, None, None);
                        return
                    else:
                        akt = akt.prawy

    def wstaw_rek(self, klucz):
        def _wstaw(akt):
            if klucz < akt.klucz:
                if akt.lewy is None:
                    akt.lewy = BST.Node(klucz, None, None)
                else:
                    _wstaw(akt.lewy)
            elif klucz > akt.klucz:
                if akt.prawy is None:
                    akt.prawy = BST.Node(klucz, None, None)
                else:
                    _wstaw(akt.prawy)
        if self.korzen is None:
            self.korzen = BST.Node(klucz, None, None)
        else:
            _wstaw(self.korzen)

    def items(self):  # wszystkie elementy in-order
        def _items(akt, x):
            if akt is None:
                return
            _items(akt.lewy, x)
            x.append(akt.klucz)
            _items(akt.prawy, x)

        x = []
        _items(self.korzen, x)
        return x

    def __repr__(self):
        x = self.items()
        return "BST(" + repr(x) + ")"

    def __iter__(self):
        "wersja bez rekurencji wymaga stosu (LIFO)"
        todo = [self.korzen]
        while todo:  # to jest przeszukiwanie w głąb ("pre-order")
            akt = todo.pop()
            if akt is None:
                continue
            todo.append(akt.prawy)
            todo.append(akt.lewy)
            yield akt.klucz

    def zdejmij_min(self):
        assert self.korzen is not None
        if self.korzen.lewy is None:
            wynik = self.korzen.klucz
            self.korzen = self.korzen.prawy
            return wynik
        else:
            akt = self.korzen
            while akt.lewy.lewy is not None:
                akt = akt.lewy
            klucz = akt.lewy.klucz
            akt.lewy = akt.lewy.prawy
            return klucz

def main():
    t = BST()
    for e in [6, 3, 4, 13, 19, 9, 11, 12, 7]:
        t.wstaw(e)
    print(t.czy_istnieje(2))
    # False
    print(t.czy_istnieje_rek(6))
    # True
    print(t)
    # BST([3, 4, 6, 7, 9, 11, 12, 13, 19])
    t.wstaw_rek(10)
    print(t)
    # BST([3, 4, 6, 7, 9, 10, 11, 12, 13, 19])
    for e in t:
        print(e, end=", ")
    # 6, 3, 4, 13, 9, 7, 11, 10, 12, 19,
    print()
    while not t.czy_pusty():
        print(t.zdejmij_min(), end=", ")
    # 3, 4, 6, 7, 9, 10, 11, 12, 13, 19,

if __name__ == "__main__":
    main()