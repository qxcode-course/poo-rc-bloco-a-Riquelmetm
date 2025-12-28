class Calculadora:
    def __init__(self, bateriamax:int):
        self.bateriamax = bateriamax
        self.bateria = 0
        self.display = 0
    
    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.bateria}"

    def carga(self, carga:int):
        if carga > self.bateriamax:
            return
        self.bateria += carga
    
    def somar(self, a:int, b:int):
        if self.bateria <=0:
            print("fail: bateria insuficiente.")
            return
        self.display = a + b
        self.bateria -= 1
    