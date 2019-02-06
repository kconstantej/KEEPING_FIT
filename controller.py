import model


class control:
    def __init__(self, peso, altura, nombre,bol):
        self.peso = float(peso)
        self.altura = float(altura)
        self.path = r"C:\Users\Pc\Downloads"
        self.nombre= nombre
        self.estado = ""
        self.bol= bol
        self.a = model.Archivo()


    def defineEstado(self):
        e = self.peso / ((self.altura / 100) ** 2)
        print(e)
        s=""
        if e < 16.00:
            s = self.a.delgadesSevera(self.path,self.nombre,self.bol)
            return s
        if e >= 16.00 and e < 18.49:
            s = self.a.delgadesModerada(self.path,self.nombre,self.bol)
            return s
        if e >= 18.50 and e < 25.00:
            s = self.a.pesoNormal(self.path,self.nombre,self.bol)
            return s
        if e >= 25.00 and e < 35.00:
            s = self.a.sobrepeso(self.path,self.nombre,self.bol)
            return s
        if e >= 35:
            print("ken--------------")
            s = self.a.obesidad(self.path,self.nombre,self.bol)
            return s
        return s