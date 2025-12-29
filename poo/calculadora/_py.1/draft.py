class Calculadora:
    def __init__(self, bateriamax:int):
        self.bateriamax = bateriamax
        self.bateria = 0
        self.display = 0
    
    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.bateria}"

    def carga(self, carga:int):
        self.bateria += carga
        if self.bateria > self.bateriamax:
            self.bateria = self.bateriamax
    
    def somar(self, a:int, b:int):
        if self.bateria <=0:
            print("fail: bateria insuficiente.")
            return
        self.display = a + b
        self.bateria -= 1
        return self.display
    def dividir (self, den, num):
        if den == 0:
            print("fail: divisao por zero.")
            return
        elif self.bateria <= 0:
             print("fail: bateria insuficiente.")
             return
        self.display = num / den
        return self.display

def main():
    while True:
        sla = input()
        print ("$" + sla)
        z = sla.split(" ")

        if z[0] == "init":
            calculadora = Calculadora(int(z[1]))

        elif z[0] == "end":
            break
        
        elif z[0] == "charge":
            calculadora.carga(int(z[1]))

        elif z[0] == "show":
            print(calculadora)
        
        elif z[0] == "sum":
            calculadora.somar(int(z[1]), int(z[2]))
        
        elif z[0] == "div":
            calculadora.dividir(int(z[1]), int(z[2]))

main()