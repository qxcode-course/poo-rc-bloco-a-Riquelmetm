class Animal:
    def __init__(self, species: str ="", age: int=0, sound: str=""):
        self.species = species
        self.age = age
        self.sound = sound
    
    def mostrar_animal (self):
        print("{species}, {age}, {sound}" )
