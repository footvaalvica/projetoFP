class conjunto:
    def __init__(self, *els):
        self.c = []
        for el in els:
            if el not in self.c:
                self.c.append(el)

    def duplica(self):
        return conjunto(*self.c)

    def insere(self, el):
        if el not in self.c:
            self.c = self.c.append(el)
        return self

    def el_conj(self):
        import random
        return random.choice(self.c)

    def cardinal(self):
        return len(self.c)

    