from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol", añosPracticando)
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil

    def getGolesMarcados(self):
        return self.__golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetasRojas

    def getPiernaHabil(self):
        return self.__piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
