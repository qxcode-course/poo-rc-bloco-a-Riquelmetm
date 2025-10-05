class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        return 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            self.wetness = self.getMaxWetness()
            print("toalha encharcada")

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0

    def __str__(self) -> str:
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"


def main():
    towel = None
    while True:
        line = input().strip()
        if line == "":
            continue
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "criar":
            color = args[1]
            size = args[2]
            towel = Towel(color, size)

        elif cmd == "mostrar":
            if towel is None:
                print("fail: toalha nao criada")
            else:
                print(towel)

        elif cmd == "seca":
            if towel is None:
                print("fail: toalha nao criada")
            else:
                if towel.isDry():
                    print("sim")
                else:
                    print("nao")

        elif cmd == "enxugar":
            if towel is None:
                print("fail: toalha nao criada")
            else:
                amount = int(args[1])
                towel.dry(amount)

        elif cmd == "torcer":
            if towel is None:
                print("fail: toalha nao criada")
            else:
                towel.wringOut()

        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
