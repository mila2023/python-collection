
class ListaWiazana:
    __slots__ = ["head"]
    class Wezel:
        __slots__ = ["data", "next"]
        def __init___(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def empty(self):
        return (self.head is None)

    def push_front(self, data):
        old_head = self.head
        self.head = ListaWiazana.Wezel(data, old_head)

    def pop_front(self):
        assert self.head is not None
        data = self.head.data
        self.head = self.head.next
        return data

def main():

    #stos: push(), pop(), empty()
    #kolejka: enqueue() - dodaj el na koniec kokejki, dequeue - pobierz i usun el z przodu kolejki, empty()
    #lista wiazana
    l = ListaWiazana()
    for i in range(5):
        l.push_front(i)
    while not l.empty():
        print(l.pop_front(), end=", ")


if __name__=="__main__":
    main()