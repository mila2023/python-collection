import ctypes

# n = 3
# t = (ctypes.py_object * n)()
#
# print(t)
# print(len(t))
# t[0] = 5
# t[1] = "napis"
# t[2] = (1,2,3)
# print(t[0],"  ",t[1],"  ",t[2])

class Tablica:

    def  __init__(self, n = 0, v = None ):

        if type(n) != int:
            raise TypeError("n nie jest int")
        if n < 0:
            raise ValueError("n jest ujemne")

        self.__dlugosc = n
        self.__dane = (ctypes.py_object * n)()
        for i in range(n):
            self.__dane[i] = v

    def __len__(self):
        #return len(self.__dane)
        return self.__dlugosc

    def  __repr__(self):
        wynik = "Tablica("
        for i in range(self.__dlugosc):
            if i > 0:
                wynik += ','
            wynik += str(self.__dane[i])
        wynik += ")"
        return wynik

    def __getitem__(self, i):

        if type(i) != int:
            raise TypeError("i musi być int")
        if not 0 <= i < len(self):
            raise IndexError()
        return self.__dane[i]

    def __setitem__(self, i, v):

        if type(i) != int:
            raise TypeError("i musi być int")
        if not 0 <= i < len(self):
            raise IndexError()
        self.__dane[i] = v

    def __iter__(self):
        for i in range(len(self)):
            yield self.__dane[i]

    def insert(self, i, v):
        if type(i) != int:
            raise TypeError("i musi być int")
        if not 0 <= i < len(self):
            raise IndexError()

        n = len(self)

        stare_dane = self.__dane
        self.__dane = (ctypes.py_object*(n+1))()
        print(f"rozmiar nowej tab = {len(self.__dane)}")
        for j in range(0,i):
            self.__dane[j] = stare_dane[j]
        self.__dane[i] = v
        for j in range(i+1, n+1):
            print(j)
            self.__dane[j] = stare_dane[j-1]


t = Tablica(3,5)
print(t)
t.insert(2,100)
print(t)
for el in t:
    print(el, end = " ")
print("")
# print(t)
# Tablica(4)
# żeby znaleźć len(t) potrzebujemy metody __len__, a t[i] - __get cośtamt
print(len(t))
t = Tablica(8,5)
print(len(t))
print(t)
print(t[3])
t[1] = 100
t[4] = 900
print(t)
