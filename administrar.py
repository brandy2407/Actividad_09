from particula import Particula 

 class Administrar
    def __init__(self):
        self.administrar = []
    def agregar_inicio(self,particula):
        self.administrar.insert(0,particula)
    def agregar_final(self,particula):
        self.administrar.append(particula)
    def mostrar(self):
        for particula in self.administrar:
         print(particula)

particula_1 = Particula(5,10,100,55)
particula_2 = Particula(5,10,20,100)
administrar_1 = Administrar()
administrar_1.agregar_inicio(particula_1)
administrar_1.agregar_final(particula_2)
administrar_1.agregar_final(particula_1)
administrar_1.mostrar() 
