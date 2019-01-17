import model


class control:
    def __init__(self, peso, altura, path):
        self.peso = float(peso)
        self.altura = float(altura)
        self.path = path
        self.estado = ""
        self.a = model.Archivo()
        self.defineEstado()

    def defineEstado(self):
        e = self.peso / ((self.altura / 100) ** 2)
        print(e)
        if e < 16.00:
            self.a.delgadesSevera(self.path)
        if e >= 16.00 and e < 18.49:
            self.a.delgadesModerada(self.path)
        if e >= 18.50 and e < 25.00:
            self.a.pesoNormal(self.path)
        if e >= 25.00 and e < 35.00:
            self.a.sobrepeso(self.path)
        if e >= 35:
            self.a.obesidad(self.path)


c = control(20, 180, "D:")
print(c.estado)
