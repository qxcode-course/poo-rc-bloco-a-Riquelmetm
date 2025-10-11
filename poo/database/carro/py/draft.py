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
        if self.pass_ >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.pass_ += 1

    def leave(self):
        if self.pass_ <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pass_ -= 1

    def fuel(self, qtd: int):
        self.gas += qtd
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, dist: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if self.gas >= dist:
            self.gas -= dist
            self.km += dist
        else:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas
            self.gas = 0


def main():
    carro = Carro()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            carro.fuel(int(args[1]))
        elif args[0] == "drive":
            carro.drive(int(args[1]))


if __name__ == "__main__":
    main()
