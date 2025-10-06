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
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pass_ -= 1

    def fuel(self, qtd: int):
        # adiciona qtd ao tanque; descarta excesso
        if qtd <= 0:
            return
        self.gas += qtd
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distancia: int):
        if self.pass_ == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if self.gas >= distancia:
            self.gas -= distancia
            self.km += distancia
        else:

            percorrido = self.gas
            self.km += percorrido
            self.gas = 0
            print(f"fail: tanque vazio apos andar {percorrido} km")


def main():
    carro = Carro()
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if not line:
            continue

        parts = line.split()
        cmd = parts[0]

        if cmd.startswith("$"):
            cmd = cmd[1:]

        if cmd == "end":
            break

        elif cmd == "show":
            print(carro)

        elif cmd == "enter":
            carro.enter()

        elif cmd == "leave":
            carro.leave()

        elif cmd == "fuel":
            if len(parts) >= 2:
                try:
                    qtd = int(parts[1])
                except:
                    continue
                carro.fuel(qtd)

        elif cmd == "drive":
            if len(parts) >= 2:
                try:
                    dist = int(parts[1])
                except:
                    continue
                carro.drive(dist)

        else:
            continue


if __name__ == "__main__":
    main()
