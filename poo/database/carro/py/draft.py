class Carro:
    def __init__(self):
        self.pass_ = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100
    def __str__(self) -> str:
        return f"pass: {self.pass_}, gas: {self.gas}, km: {self.km}"
    def enter(self):
        self.pass_ +=1
        if self.pass_ >= self.passMax:
            print("fail: limite de pessoas atingido")
            self.pass_ -=1
    def leave(self):
        self.pass_ -=1
        if self.pass_ <= 0:
            print("fail: nao ha ninguem no carro")
    def fuel_increment(self):
        self.gas = int(input())
        if self.gas > self.gasMax:
            self.gas = self.gasMax - self.gas
    def drive_distance(self, distancia:int):
        if self.pass_ <=0:
            print("fail: não há ninguém no carro")
            return
        if self.gas <=0:
            print("fail: tanque vazio")
            return
        if self.gas > distancia:
            self.km = distancia
            self.gas -= distancia
        else:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0


        

def main():
    while True :
        print(Carro)
        print("oi")
    

