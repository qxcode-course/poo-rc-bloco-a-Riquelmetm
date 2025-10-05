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
    def leave(self):
        self.pass_ -=1
        if self.pass_ <= 0:
            print("fail: nao ha ninguem no carro")
    
