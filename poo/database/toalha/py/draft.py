class Towell:
    def __init__(self, color: str = "", size: str = ""):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxwetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0  # Valor padrão para tamanhos não reconhecidos

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.getMaxwetness():
            self.wetness = self.getMaxwetness()
            print("toalha encharcada")

    def wringOut(self) -> None:
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0

    def show(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.color} {self.size} {self.wetness}"


def main():
    towel: Towell = Towell("", "")
    while True:
        line: str = input("Digite um comando: ")
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "new":
            if len(args) < 3:
                print("fail: comando 'new' necessita de 2 argumentos.")
                continue
            color: str = args[1]
            size: str = args[2]
            towel = Towell(color, size)
        elif args[0] == "show":
            print(towel)  # Aqui imprime o objeto towel, chamando o método
        else:
            print("fail: comando não encontrado")


if __name__ == "__main__":
    main()
