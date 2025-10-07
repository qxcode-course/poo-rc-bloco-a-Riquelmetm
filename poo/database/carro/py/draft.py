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
        if self.pass_ > self.passMax:
            print("fail: limite de pessoas atingido")
            self.pass_ -=1
    def leave(self):
        if self.pass_ <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pass_ -= 1
    def fuel_increment(self,fuel:int):
        self.gas = fuel
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
    carro = Carro()

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "fuel":
            fuel = int(input())
            carro.fuel_increment(fuel)
        if args[0] == "show":
            print(carro)
        if args[0] == "leave":
            carro.leave()
        if args[0] == "enter":
            carro.enter()
        if args[0] == "drive":
            distancia = int(input())
            carro.drive_distance(distancia)



main()

